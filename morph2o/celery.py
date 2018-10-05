from __future__ import absolute_import, unicode_literals
from datetime import timedelta
#from visualizer import tasks
import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'morph2o.settings')

#from django.conf import settings  # noqa

#settings.configure()
app = Celery('morph2o', broker='pyamqp://')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
#app.conf.update(
#	CELERY_RESULT_BACKEND='django-db',)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.beat_schedule = {
#     'hourly-download': {
#         'task': 'visualizer.tasks.download',
#         'schedule': 3600.0
#     },
    'hourly-async-download': {
        'task': 'visualizer.tasks.async_download',
        'schedule': crontab(minute='*/15')
    },
    'hourly-async-update':{
        'task': 'visualizer.tasks.async_update',
        'schedule': crontab(minute='2,17,32,47')
    },
}
#app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
