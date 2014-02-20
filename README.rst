Philip's "mezzanine template"
============================


This template is a good starting point for an Mezzanine_ based project.
Your modifications should go to the app `_site` or the module `envs`.

The template is prepared for use with:

- S3 Storage
- django-golive_ for deployment
- Debug toolbar
- Django extensions
- django-nose
- Redis cache

Create a project
--------------
.. code:: bash

 V=v`curl https://raw.github.com/fatrix/mezzanine_example/master/VERSION` && tempdir=`mktemp -d -t tmp` &&  mpwd=`pwd` &&  wget https://api.github.com/repos/fatrix/mezzanine_example/tarball/$V -O $tempdir/mezzanine_example-$V.tgz && cd $tempdir && tar -zxf $tempdir/mezzanine_example-$V.tgz --strip-components=1 '*/project_template' && cd - && django-admin.py startproject --template=$tempdir/project_template testsite && echo rm -rf $tempdir

URL's
-----
 `_site/urls.py`

Additional modules
------------------
 `_site/requirements.txt`

Overwrite templates
-------------------
 `_site/templates/..`

Settings
--------
 `envs/ENV_ID` (See django-golive_.)

.. _django-golive: https://github.com/fatrix/django-golive
.. _Mezzanine: http://mezzanine.jupo.org/
.. _hyperlink-name: http://sahli.net

Versions
--------
Master 
~~~~~~
Mezzanine 3.0.9

... and some more ...