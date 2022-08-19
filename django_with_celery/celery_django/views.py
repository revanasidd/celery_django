from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from celery_django.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from django.utils import timezone
# Create your views here.
# @shared_task(bind=True)
# def send_mail_func(self):
def send_mail_func():
    starts_now = timezone.now() + timezone.timedelta(minutes=360)
    print(f'11-----------',starts_now)
    time_diffrenece = starts_now - (timezone.now()+timezone.timedelta(minutes=330))
    print(f'11-----{time_diffrenece}----{timezone.now()+timezone.timedelta(minutes=330)}----',starts_now)

