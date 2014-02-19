import datetime
from boto.utils import ISO8601, ISO8601_MS, logging
from filebrowser_safe.storage import S3BotoStorageMixin
from storages.backends.s3boto import S3BotoStorage, parse_ts_extended
from django.conf import settings

import boto
boto.set_stream_logger('aws')


class FixedS3BotoStorage(S3BotoStorage, S3BotoStorageMixin):
    def url(self, name):
        url = super(FixedS3BotoStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url

    def modified_time(self, name):
        """
        Fixes the None timestamp issue:
        https://groups.google.com/forum/#!msg/mezzanine-users/CQTvNmFa1f8/UYL5WI7po70J
        https://bitbucket.org/david/django-storages/issue/163/s3boto-modified_time-fails-for-new-file
        """
        name = self._normalize_name(self._clean_name(name))
        entry = self.entries.get(name)
        # only call self.bucket.get_key() if the key is not found
        # in the preloaded metadata.
        if entry is None:
            entry = self.bucket.get_key(self._encode_name(name))
            # Parse the last_modified string to a local datetime object.
        if not entry.last_modified:
            try:
                entry.last_modified = datetime.datetime.now().strftime(ISO8601)
            except ValueError:
                entry.last_modified = datetime.datetime.now().strftime(ISO8601_MS)
        return parse_ts_extended(entry.last_modified)


    @property
    def connection(self):
        debug_level = getattr(settings, 'AWS_DEBUG', 0)
        if self._connection is None:
            self._connection = self.connection_class(
                self.access_key, self.secret_key,
                calling_format=self.calling_format, debug=debug_level)
        return self._connection

def set_stream_logger(name, level=logging.DEBUG, format_string=None):
    global log
    if not format_string:
        format_string = "%(asctime)s %(name)s [%(levelname)s]:%(message)s"
    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    log = logger

from mezzanine.core import views

import os
try:
    from urllib.parse import urljoin, urlparse
except ImportError:
    from urlparse import urljoin, urlparse

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.staticfiles import finders
from django.http import HttpResponse

def static_proxy(request):
    """
    Serves TinyMCE plugins inside the inline popups and the uploadify
    SWF, as these are normally static files, and will break with
    cross-domain JavaScript errors if ``STATIC_URL`` is an external
    host. URL for the file is passed in via querystring in the inline
    popup plugin template, and we then attempt to pull out the relative
    path to the file, so that we can serve it locally via Django.
    """
    normalize = lambda u: ("//" + u.split("://")[-1]) if "://" in u else u
    url = normalize(request.GET["u"])
    host = "//" + request.get_host()
    netloc = urlparse(request.GET['u']).netloc
    static_url = normalize(settings.STATIC_URL)
    for prefix in (host, static_url, "//", netloc, "/"):
        if url.startswith(prefix):
            url = url.replace(prefix, "", 1)

    # if is remote
    #schemes = urlparse(request.GET['u']).scheme
    #if "http" or "https" in schemes:
    #    url = urlparse(request.GET['u']).path.replace("/", "", 1)

    response = ""
    mimetype = ""
    path = finders.find(url)
    if path:
        if isinstance(path, (list, tuple)):
            path = path[0]
        if url.endswith(".htm"):
            # Inject <base href="{{ STATIC_URL }}"> into TinyMCE
            # plugins, since the path static files in these won't be
            # on the same domain.
            static_url = settings.STATIC_URL + os.path.split(url)[0] + "/"
            if not urlparse(static_url).scheme:
                static_url = urljoin(host, static_url)
            base_tag = "<base href='%s'>" % static_url
            mimetype = "text/html"
            with open(path, "r") as f:
                response = f.read().replace("<head>", "<head>" + base_tag)
        else:
            mimetype = "application/octet-stream"
            with open(path, "rb") as f:
                response = f.read()
    return HttpResponse(response, content_type=mimetype)

views.static_proxy = staff_member_required(static_proxy)

def show_toolbar_for_admin(request):
    if request.user.is_authenticated():
        return request.user.is_staff
    else:
        return False