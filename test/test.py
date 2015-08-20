�         ���    -*-
import requests
import random
from datetime import datetime, timedelta


def send_disk_status():
    now = datetime.now()
    for i in xrange(50):
        r = requests.post('http://localhost:5000/api/push_disk_status', data={
            'uid': 5,
            'used': 70 - i + random.randint(0, 30),
            'total': 100,
            'time': (now - timedelta(i)).strftime("%Y-%m-%d %H:%I:%S")
        })
        print r.status_code, r.text


def send_upload_status():
    pass


send_disk_status()

