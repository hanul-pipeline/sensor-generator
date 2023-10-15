from sensors import create_sensor_data

# location 정보
location_id = 100
location_name = "location"

# sensor 데이터 생성기
def sensor_100():
    from time import time, sleep

    # only for test
    import random

    # sensor 정보
    sensor_id = 100
    sensor_name = "sensor_name"
    unit = "unit"
    type_id = "type_id"
    type_name = "type_name"

    is_running = True

    try:
        while is_running:
            start_time = time()

            # Perform your measurement and jobs

            measurement = random.randrange(0, 50)
            network_name = "network_name"
            network_strength = "network_strength"

            dict = create_sensor_data(measurement, network_name, network_strength, 
                              type_name, type_id, location_name, location_id,
                              sensor_name, sensor_id, unit)
            
            yield {"dict" : dict}

            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False

        # Perform any cleanup or additional jobs
