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

    # test: 센서 데이터 랜덤 생성기
    import numpy as np

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

            # 측정값
            measurement = []
            temperature = np.random.randint(15, 50, (8, 8))
            measurement.append({
                "value_type": "temperature",
                "value": temperature,
                "unit": "°C",
                "count": 64,
                "percentage": 50})

            # 네트워크 정보
            network_info = get_internet_connection_info()
            network_name = network_info["name"]
            network_strength = network_info["dB"]

            # 인스턴스 데이터 생성
            dict_measurement = create_dict_measurement(measurement, network_name, network_strength, 
                              sensor_type, location_name, location_id,
                              sensor_name, sensor_id)

            # alert logic
            alert = create_alert(dict_measurement, location_id)

            # 데이터 저장
            yield {"dict_measurement": dict_measurement, "alert": alert}

            # time sleep
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False


