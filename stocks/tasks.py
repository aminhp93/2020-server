from django_rq import job
from datetime import datetime, timedelta
import pytz

@job('test')
def test1():
    now = datetime.now()
    print(8, 'test1', now.year, now.month, now.day, now.hour, now.minute, now.second, pytz.UTC)

    print('test ==============')