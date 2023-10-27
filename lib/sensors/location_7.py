from sensors import create_sensor_data, get_sensor_information
import gc

location_id = 7
location_name = "도장공정"

# 열화상카메라
def sensor_100():
    from time import time, sleep
    from wifi_information import get_internet_connection_info

    # test: 센서 데이터 랜덤 생성기
    import numpy as np

    # default
    sensor_id = 100
    sensor_name = "AMG-8833"
    sensor_type = "열화상카메라"
    total_cnt = 64
    percentage = 50

    is_running = True

    try:
        while is_running:
            start_time = time()

            # garbage collector
            gc.collect()

            # 측정값
            measurement = []
            temperature = np.random.randint(15, 36, (8, 8))
            measurement.append({
                "value_type": "temperature",
                "value": temperature,
                "unit": "°C",
                "count": 64})
            
            for data in measurement:
                

            # 네트워크 정보
            network_info = get_internet_connection_info()
            network_name = network_info["name"]
            network_strength = network_info["dB"]

            # 인스턴스 데이터 생성
            dict = create_sensor_data(measurement, network_name, network_strength, 
                              sensor_type, location_name, location_id,
                              sensor_name, sensor_id)
            
            # 데이터 저장
            yield {"dict" : dict}

            # time sleep
            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False


