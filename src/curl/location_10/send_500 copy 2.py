from configparser import ConfigParser
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, f'../../../config/config.ini')
module_dir = os.path.join(current_dir, f'../../../lib/sensors')
sys.path.append(module_dir)

from location_7 import sensor_500
from sensors import send_curl, send_alert

config = ConfigParser()
config.read(config_dir)
url = config.get("FastAPI", "url")

# URL 및 데이터 설정
url = f"{url}/load/100"

# 헤더 설정
headers = {"Content-Type": "application/json"}

for status in sensor_500():
    # send_curl(url, headers, status)
    # send_alert(url, headers, status)
    send_curl(headers=headers, status=status)
    send_alert(headers=headers, status=status)