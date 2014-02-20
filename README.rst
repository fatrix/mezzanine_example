Philip's "mezzanine template"
============================


This template is a good starting point for an Mezzanine_ based project.
Your modifications should go to the app `_site` or the module `envs`.

The template is prepared for use with:

- S3 Storage
- django-golive_ for deployment
- django-debugtoolbar_
- django-extensions_
- django-nose
- Redis cache

Create a project
--------------

Create a project from the template with following command. In your activated virtualenv only Django version 1.6.2 must be installed

.. code:: bash

 virtualenv --no-site-packages $HOME/virtualenvs/myenv
 . $HOME/virtualenvs/myenv/bin/activate
 pip install Django==1.6.2

.. code:: bash

 V=v`curl https://raw.github.com/fatrix/mezzanine_example/master/VERSION` && tempdir=`mktemp -d -t tmp` &&  mpwd=`pwd` &&  wget https://api.github.com/repos/fatrix/mezzanine_example/tarball/$V -O $tempdir/mezzanine_example-$V.tgz && cd $tempdir && tar -zxf $tempdir/mezzanine_example-$V.tgz --strip-components=1 '*/project_template' && cd - && django-admin.py startproject --template=$tempdir/project_template testsite && echo rm -rf $tempdir

URL's
-----

Put additionals urls to 

 `_site/urls.py`

Additional modules
------------------

Your required python modules goes to

 `_site/requirements.txt`

Overwrite templates
-------------------

Custom templates and overwrites in 

 `_site/templates/..`

Settings
--------

Settings are in the envs module. There are for every stage a module.

 `envs/ENV_ID` (See django-golive_.)

Start runserver with the option --settings:

.. code:: bash

 python manage.py runserver --settings=envs.local

.. _django-golive: https://github.com/fatrix/django-golive
.. _Mezzanine: http://mezzanine.jupo.org/
.. _hyperlink-name: http://sahli.net
.. _django-extensions: http://django-extensions.readthedocs.org/en/latest/
.. _django-debugtoolbar: http://django-debug-toolbar.readthedocs.org/en/1.0/

Versions
--------
Master 
~~~~~~
Mezzanine 3.0.9

... and some more ...
