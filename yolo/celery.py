import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yolo.settings')
app = Celery('yolo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
