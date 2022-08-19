from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_with_celery import settings
from django.utils import timezone
from datetime import timedelta
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# @shared_task(bind=True)
def send_mail_func_seted_minutes():
    print(f'12-----------')
    users = get_user_model().objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hi! This My Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"
    print('done--------------')
@shared_task(bind=True)
def send_mail_func(self):
# def send_mail_func():
    schedule,created = CrontabSchedule.objects.get_or_create(hour=18,minute=10,day_of_month=6,day_of_week=8,month_of_year=2022)
    import random
    random_num =random.randint(10, 20)
    task_name = f'test_task {random_num}'
    print(f'31--------{schedule}-----------{created}------------------')
    task_obj = PeriodicTask.objects.create(crontab=schedule,name=task_name,task='celery_django.tasks.send_mail_func_seted_minutes')
    print(f'34------------',task_obj)