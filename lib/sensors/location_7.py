from time import time, sleep
from datetime import datetime
import gc
import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, f'../modules')
sys.path.append(module_dir)

from grade import *
from sensors import *
from wifi_information import get_internet_connection_info

# demo
from demo import *

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
            measurement_check = []
            
            # def max_value         
            if datetime.now().strftime('%Y-%m-%d') == "2023-12-13":
                if datetime.now().strftime('%H') == "17":
                    mid_value = round(30 + (0.001*cnt), 3)
                elif datetime.now().strftime('%H') == "18":
                    mid_value = round(34 + (0.004*cnt), 3)
                elif datetime.now().strftime('%H') == "19":
                    mid_value = round(75 + (8.28*cnt), 3)
                    if cnt == 90:
                        break
            else:
                mid_value = 30

            # add measurements
            temperature = generate_matrix(8, 8, mid_value-0.5, mid_value+0.5)
            measurement.append({
                "value_type": "temperature",
                "value": f"{temperature.tolist()}",
                "unit": "°C",
                "cnt": 64,
                "percentage": 50})
            measurement_check.append({
                "value_type": "temperature",
                "value": temperature,
                "unit": "°C",
                "cnt": 64,
                "percentage": 50})

            # network information
            network_info = get_internet_connection_info()
            network_name = network_info["name"]
            network_strength = network_info["dB"]

            # create instance data: measurement
            dict_measurement = create_dict_measurement(measurement, network_name, network_strength, 
                              sensor_type, location_name, location_id,
                              sensor_name, sensor_id)
            
            dict_check = create_dict_measurement(measurement_check, network_name, network_strength, 
                              sensor_type, location_name, location_id,
                              sensor_name, sensor_id)

            # create instance data: alert
            alert = create_alert(dict_check, location_id)

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


# confirmed
def sensor_500():
    from time import time, sleep

    import random # for test: sensor data generator

    # default
    sensor_id = 500
    sensor_name = "DHT-21"
    sensor_type = "온습도 센서"

    is_running = True
    cnt = 0

    try:
        while is_running:
            start_time = time()

            # update count
            cnt += 1

            # garbage collector 
            gc.collect()
                
            if datetime.now().strftime('%Y-%m-%d') == "2023-12-13":
                if datetime.now().strftime('%H') == "17":
                    temp_mid = 18 + (cnt*0.00005)
                    moist_mid = 50 - (cnt*0.0014)
                elif datetime.now().strftime('%H') == "18":
                    temp_mid = 20 + (cnt*0.0042)
                    moist_mid = 45 - (cnt*0.0028)
                elif datetime.now().strftime('%H') == "19":
                    temp_mid = 40 + (cnt*4.55)
                    moist_mid = 35 - (cnt*0.33)
                    if cnt == 90:
                        break
            else:
                temp_mid = 18
                moist_mid = 50

            # measurement
            measurement = []
            temperature = round(random.uniform(temp_mid-0.5, temp_mid+0.5), 2) # for test: sensor data generator
            measurement.append({
                "value_type": "temperature",
                "value": temperature,
                "unit": "°C",
                "cnt": 1,
                "percentage": 0})

            moisture = round(random.uniform(moist_mid-0.5, moist_mid+0.5), 2) # for test: sensor data generator
            measurement.append({
                "value_type": "moisture",
                "value": moisture,
                "unit": "%",
                "cnt": 1,
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

            # check cnt
            if cnt == 3600:
                break

            # time sleep
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False



# confirmed
def sensor_600():
    from time import time, sleep

    import random # for test: sensor data generator

    # default
    sensor_id = 600
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
            
            # def max_value              
            if datetime.now().strftime('%Y-%m-%d') == "2023-12-13":
                if datetime.now().strftime('%H') == "17":
                    mid_value = round(0.1 + (0.00003*cnt), 4)
                elif datetime.now().strftime('%H') == "18":
                    mid_value = round(0.2 + (0.00003*cnt), 4)
                elif datetime.now().strftime('%H') == "19":
                    mid_value = round(0.8 + (0.028*cnt), 4)
                    if cnt == 90:
                        break
            else:
                mid_value = 30

            # measurement
            measurement = []
            CH4 = round(random.uniform(mid_value-0.01, mid_value+0.01), 2) # for test: sensor data generator
            measurement.append({
                "value_type": "CH4",
                "value": CH4,
                "unit": "ppm",
                "cnt": 1,
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

            # check cnt
            if cnt == 3600:
                break

            # time sleep
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False