from datetime import datetime
import re
import time
import random
import numpy as np
import requests as rq
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print(datetime.today().date())
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSe-qq4DeiVESiRUDCAfSKUbqcJrvsu8GgefIKl67u05Eu3jXw/formResponse'

    payload = {
        'entry.326242429' : '', # name
        'entry.1588677691_year' : '',
        'entry.1588677691_month' : '',
        'entry.1588677691_day' : '',
        'entry.1139224151' : '', # ...
        'entry.522407608' : '',
        'entry.2113889508' : '',
        'fvv' : '0',
        'draftResponse' : '[]',
        'pageHistory' : '0',
        'fbzx' : '1436722322797533594'
    }

    try:
        payload['entry.326242429'] = 'XXX' # 名字記得自己改啊
        payload['entry.1588677691_year'] = str(datetime.today().year)
        payload['entry.1588677691_month'] = str(datetime.today().month)
        payload['entry.1588677691_day'] = str(datetime.today().day)
        payload['entry.1139224151'] = '否'
        payload['entry.522407608'] = '否'
        payload['entry.2113889508'] = '否'
        res = rq.post(url, data=payload)
        res.raise_for_status()
        if res.status_code == 200 :
            time.sleep(5)
    except rq.HTTPError:
        print('HTTP Error!')

def dojob():
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', days=1, id='AILab_google_forum')
    scheduler.start()

if __name__=='__main__':
    dojob()