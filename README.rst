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

Create project
--------------
.. code:: bash

 tempdir=`mktemp -d -t tmp` &&  mpwd=`pwd` &&  wget https://api.github.com/repos/fatrix/mezzanine_example/tarball/0.2 -O $tempdir/mezzanine_example-0.2.tgz && cd $tempdir && tar -zxf $tempdir/mezzanine_example-0.2.tgz && cd - && django-admin.py startproject --template=$tempdir/fatrix-mezzanine_example-*/project_template/ testsite && echo rm -rf $tempdir

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