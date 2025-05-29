# author xiaogang
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'city_work.settings')

app = Celery('city_work')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

