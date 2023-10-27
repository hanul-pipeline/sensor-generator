import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, f'../../lib/sensors')
sys.path.append(module_dir)

from location_100 import sensor_500
from sensors import send_curl, send_alert

# URL 및 데이터 설정
url = "http://222.108.81.83:4000/endpoint"

# 헤더 설정
headers = {"Content-Type": "application/json"}

for status in sensor_500():
    send_curl(url, headers, status)
    send_alert(url, headers, status)