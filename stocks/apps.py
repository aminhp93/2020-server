from django.apps import AppConfig
import django_rq
from datetime import datetime, timedelta
import pytz
from . import tasks

class StocksConfig(AppConfig):
    name = 'stocks'

    def ready(self):
        
        now = datetime.now()
        print(16, 'ready', now.year, now.month, now.day, now.hour, now.minute, now.second, pytz.UTC)
        scheduler = django_rq.get_scheduler('test')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            scheduler.cancel(job)
            job.delete()
        minute = 34
        scheduled_time = datetime(now.year, now.month, now.day, now.hour, minute, 0, 0, tzinfo=pytz.UTC)
        print(scheduled_time)
        scheduler.schedule(
            scheduled_time=scheduled_time,
            func=tasks.test1,
            interval=2
        )



