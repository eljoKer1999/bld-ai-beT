import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')

app.config_from_object('django.conf:settings', namespace='CELERY_CONF')

app.autodiscover_tasks()

app.conf.beat_schedule = settings.CELERY_CONF_BEAT_SCHEDULE


