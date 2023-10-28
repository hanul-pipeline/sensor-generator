from time import time, sleep
import gc
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, f'../modules')
sys.path.append(module_dir)

from grade import *
from sensors import *
from wifi_information import get_internet_connection_info


location_id = 7
location_name = "도장공정"


# confirmed
def sensor_100():
    
    import numpy as np # for test: sensor data generator

    # default
    sensor_id = 100
    sensor_name = "AMG-8833"
    sensor_type = "열화상카메라"

    is_running = True

    try:
        while is_running:
            start_time = time()

            # garbage collector
            gc.collect()

            # measurement
            measurement = []
            temperature = np.random.randint(15, 35, (8, 8)) # for test: sensor data generator
            measurement.append({
                "value_type": "temperature",
                "value": temperature,
                "unit": "°C",
                "count": 64,
                "percentage": 50})

            # network information
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


# confirmed
def sensor_500():
    from time import time, sleep

    import random # for test: sensor data generator

    # default
    sensor_id = 500
    sensor_name = "DHT-21"
    sensor_type = "온습도 센서"

    is_running = True

    try:
        while is_running:
            start_time = time()

            # garbage collector 
            gc.collect()

            # measurement
            measurement = []
            temperature = random.randrange(15, 35) # for test: sensor data generator
            measurement.append({
                "value_type": "temperature",
                "value": temperature,
                "unit": "°C",
                "count": 1,
                "percentage": 0})

            moisture = random.randrange(40, 60) # for test: sensor data generator
            measurement.append({
                "value_type": "moisture",
                "value": moisture,
                "unit": "%",
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