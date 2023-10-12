type_id = 123
type_nm = "gas"

def sensor_404():
    from time import time, sleep
    from datetime import datetime

    loc_id = "<loc_id>"
    loc_nm = "<loc_nm>"
    sensor_id = "<sensor_id>"
    sensor_nm = "<sensor_nm>"
    unit = "<unit>"

    is_running = True

    try:
        while is_running:
            start_time = time()

            nowdate = datetime.now().strftime("%Y-%m-%d")
            nowtime = datetime.now().strftime("%H:%M:%S")

            # Perform your measurement and jobs

            measurement = "<measurement>"
            elapsed = "<elapsed>"
            network_nm = "<network_nm>"
            network_str = "<network_str>"

            yield {
                "type" : {"name" : type_nm, "id" : type_id},
                "nowdate": nowdate,
                "nowtime": nowtime,
                "location": {"name": loc_nm, "id": loc_id},
                "type": {"name": "gas", "id": 123},
                "data": {
                    "sensor": {"name": sensor_nm, "id": sensor_id},
                    "measurement": measurement,
                    "unit": unit,
                    "elapsed_time_sec": elapsed
                },
                "connection": {"network_name": network_nm, "signal_strength_db": network_str}
            }

            end_time = time()
            sleep(1 - (end_time - start_time))

    except KeyboardInterrupt:
        is_running = False

        # Perform any cleanup or additional jobs

if __name__ == "__main__":
    for status in sensor_404():
        print(status)
