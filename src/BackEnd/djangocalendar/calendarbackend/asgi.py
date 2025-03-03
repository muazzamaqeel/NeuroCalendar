"""
ASGI config for calendarbackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# We default to dev, but you can set DJANGO_SETTINGS_MODULE externally
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calendarbackend.settings.dev')

application = get_asgi_application()
