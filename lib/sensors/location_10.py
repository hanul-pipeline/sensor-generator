from time import time, sleep
import gc
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, f'../modules')
sys.path.append(module_dir)

from grade import *
from sensors import *
from wifi_information import get_internet_connection_info


location_id = 10
location_name = "제1 연구실"


# confirmed
def sensor_300():
    from time import time, sleep

    import random # for test: sensor data generator

    # default
    sensor_id = 300
    sensor_name = "MQ-4"
    sensor_type = "가연성 가스 센서"

    is_running = True
    cnt = 0

    try:
        while is_running:
            start_time = time()

            # update cnt
            cnt += 1

            # garbage collector 
            gc.collect()

            # measurement
            measurement = []
            CH4 = round(random.uniform(0, 1.0), 1) # for test: sensor data generator
            measurement.append({
                "value_type": "CH4",
                "value": CH4,
                "unit": "ppm",
                "cnt": 1,
                "percentage": 0})

            # metwork information
            network_info = get_internet_connection_info()
            network_name = network_info["name"]
            network_strength = network_info["dB"]

            # create instance data: measurement
            dict_measurement = create_dict_measurement(measurement, network_name, network_strength, 
                              sensor_type, location_name, location_id,
                              sensor_name, sensor_id)

            # create instance data: alert
            alert = create_alert(dict_measurement, location_id)

            # yield datas
            yield {"dict_measurement": dict_measurement, "alert": alert}

            # check cnt
            if cnt == 3600:
                break

            # time sleep
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False