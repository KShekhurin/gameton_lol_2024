from models.data_models import *
from datetime import datetime, timedelta
from time import sleep

def wait_till_nearest(nearest_round: Round):
    start = datetime.strptime(nearest_round.start_at, '%Y-%m-%dT%H:%M:%SZ')
    start += timedelta(hours=3)
    now = datetime.now()
    delta = start - now

    sleep(delta.seconds)
