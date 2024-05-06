import os

from django.core.wsgi import get_wsgi_backendlication

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

backendlication = get_wsgi_backendlication()
