from configparser import ConfigParser
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sensor_dir = os.path.join(current_dir, f'../../../lib/sensors')
sys.path.append(sensor_dir)
from location_10 import sensor_300

module_dir = os.path.join(current_dir, f'../../../lib/modules')
sys.path.append(module_dir)
from sensors import *


config_dir = os.path.join(current_dir, f'../../../config/config.ini')
config = ConfigParser()
config.read(config_dir)

uri_stream = config.get("FastAPI", "stream")
uri_alert = config.get("FastAPI", "alert")

url_stream = f"{uri_stream}/update/300"
url_alert = f"{uri_alert}/alert/10"

for status in sensor_300():
    # confirmed
    send_curl_measurement(status=status, url=url_stream)
    send_curl_alert(status=status, url=url_alert)