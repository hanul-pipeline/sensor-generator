from sensors import create_sensor_data
import gc

# location 정보
location_id = 100
location_name = "location"

# 열화상카메라
def sensor_100():
    from time import time, sleep
    from wifi_information import get_internet_connection_info

    # test: 센서 데이터 랜덤 생성기
    import numpy as np

    # sensor 정보
    sensor_id = 100
    sensor_name = "ESP-8266"
    unit = {"온도": "°C"}
    sensor_type = "열화상카메라"

    # alert 정보
    type_id = 100
    type_name = "고온"

    is_running = True

    try:
        while is_running:
            start_time = time()

            # garbage collector
            gc.collect()

            # 측정값
            temperature = np.random.randint(15, 36, (8, 8))
            measurement = {"열화상카메라": temperature}

            # 네트워크 정보
            network_info = get_internet_connection_info()
            network_name = network_info["WiFi 명"]
            network_strength = network_info["신호 강도(dBm)"]

            # 인스턴스 데이터 생성
            dict = create_sensor_data(measurement, network_name, network_strength, 
                              sensor_type, location_name, location_id,
                              sensor_name, sensor_id, unit, type_id, type_name)
            
            # 데이터 저장
            yield {"dict" : dict}

            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False


# 온습도센서
def sensor_500():
    from time import time, sleep
    from wifi_information import get_internet_connection_info

    # test: 센서 데이터 랜덤 생성기
    import random

    # sensor 정보
    sensor_id = 500
    sensor_name = "DHT-21"
    unit = {"온도": "°C", "습도": "%"}
    type_name = "온습도 센서"

    is_running = True

    try:
        while is_running:
            start_time = time()

            # garbage collector 
            gc.collect()

            # 측정값
            temperature = random.randrange(15, 25)
            moisture = random.randrange(40, 60)
            measurement = {"온도": temperature, "습도": moisture}

            # 네트워크 정보
            network_info = get_internet_connection_info()
            network_name = network_info["WiFi 명"]
            network_strength = network_info["신호 강도(dBm)"]

            # 인스턴스 데이터 생성
            dict = create_sensor_data(measurement, network_name, network_strength, 
                              type_name, location_name, location_id,
                              sensor_name, sensor_id, unit)
            
            # 데이터 저장
            yield {"dict" : dict}

            # 
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False
