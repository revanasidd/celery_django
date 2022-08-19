from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
#this deault os imporetd 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_celery.settings')

app = Celery('django_with_celery')

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'celery_django.tasks.send_mail_func',
        'schedule': crontab(hour=17, minute=40),
        #'args': (2,)
    }
    
}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')