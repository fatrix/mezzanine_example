from project_example.settings import *
from golive.utils import get_var

DATABASES = {
    "default": {
        # "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "mezzanine_example_sandbox",
        # Not used with sqlite3.
        "USER": "mezzanine_example_sandbox",
        # Not used with sqlite3.
        "PASSWORD": get_var('DB_PASSWORD'),
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

DEBUG = True
ALLOWED_HOSTS = ['mezzanine-example']
