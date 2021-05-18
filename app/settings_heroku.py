from .settings import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['entertainment-db-udl.herokuapp.com']

# Configure Django App for Heroku.
django_heroku.settings(locals())
