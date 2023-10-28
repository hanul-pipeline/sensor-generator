from time import time, sleep
import gc
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, f'../modules')
sys.path.append(module_dir)

from grade import *
from sensors import *
from wifi_information import get_internet_connection_info


location_id = 11
location_name = "제2 연구실"


# confirmed
def sensor_400():
    from time import time, sleep

    import random # for test: sensor data generator

    # default
    sensor_id = 400
    sensor_name = "MQ-7"
    sensor_type = "일산화탄소 센서"


    is_running = True

    try:
        while is_running:
            start_time = time()

            # garbage collector 
            gc.collect()

            # measurement
            measurement = []
            CO = round(random.uniform(0, 300.0), 1) # for test: sensor data generator
            measurement.append({
                "value_type": "CO",
                "value": CO,
                "unit": "ppm",
                "count": 1,
                "percentage": 0})

            # get network information
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

            # time sleep
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False