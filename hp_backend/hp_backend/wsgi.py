"""
WSGI config for hp_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys

sys.path.append("/home/encode/hp_apis/hp_backend/venv/lib/python3.6/site-packages")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hp_backend.settings")

application = get_wsgi_application()
