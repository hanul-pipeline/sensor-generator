from configparser import ConfigParser
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sensor_dir = os.path.join(current_dir, f'../../../lib/sensors')
sys.path.append(sensor_dir)
from location_8 import sensor_200

module_dir = os.path.join(current_dir, f'../../../lib/modules')
sys.path.append(module_dir)
from sensors import *

# set config
config_dir = os.path.join(current_dir, f'../../../config/config.ini')
config = ConfigParser()
config.read(config_dir)

# URL 및 데이터 설정
uri_stream = config.get("FastAPI", "stream")
url_stream = f"{uri_stream}/update/200"
uri_alert = config.get("FastAPI", "alert")
url_alert = f"{uri_stream}/alert/8"

for status in sensor_200():
    send_curl_measurement(status=status, url=url_stream)
    send_curl_alert(status=status, url=url_alert)
    
