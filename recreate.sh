#!/bin/bash
rm -rf example
mkdir -p example/virtualenv
virtualenv example/virtualenv/testsite
example/virtualenv/testsite/bin/pip install Django==1.6.5
cd example
virtualenv/testsite/bin/django-admin.py startproject --template=../project_template testsite
cd testsite
../virtualenv/testsite/bin/pip install -r requirements.txt
../virtualenv/testsite/bin/python manage.py runserver
cd ../..
