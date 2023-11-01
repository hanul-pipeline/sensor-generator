from configparser import ConfigParser
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sensor_dir = os.path.join(current_dir, f'../../../lib/sensors')
sys.path.append(sensor_dir)
from location_8 import sensor_200

module_dir = os.path.join(current_dir, f'../../../lib/modules')
sys.path.append(module_dir)
from sensors import *

config_dir = os.path.join(current_dir, f'../../../config/config.ini')
config = ConfigParser()
config.read(config_dir)
url = config.get("FastAPI", "url")

# URL 및 데이터 설정
url = f"{url}/update/200"

for status in sensor_200():
    # confirmed
    send_curl_measurement(status=status, url=url)
    send_curl_alert(status=status)