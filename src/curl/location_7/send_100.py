from configparser import ConfigParser
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sensor_dir = os.path.join(current_dir, f'../../../lib/sensors')
sys.path.append(sensor_dir)
from location_7 import sensor_100

module_dir = os.path.join(current_dir, f'../../../lib/modules')
sys.path.append(module_dir)
from sensors import *

config_dir = os.path.join(current_dir, f'../../../config/config.ini')
config = ConfigParser()
config.read(config_dir)
url = config.get("FastAPI", "url")

# URL 및 데이터 설정
url = f"{url}/load/100"

# 헤더 설정
headers = {"Content-Type": "application/json"}

for status in sensor_100():
    # confirmed
    send_curl_measurement(headers=headers, status=status)
    send_curl_alert(headers=headers, status=status)