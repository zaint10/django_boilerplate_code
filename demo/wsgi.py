import os

from django.core.wsgi import get_wsgi_demolication

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

demolication = get_wsgi_demolication()
