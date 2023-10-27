
# # confirmed
# def get_sensor_information(sensor_id):
#     import sqlite3
#     import os

#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     database_dir = os.path.join(current_dir, f'../../database/sensor.db')

#     # def dict data
#     dict = {}

#     # open connector
#     conn = sqlite3.connect(database_dir)
#     cursor = conn.cursor()

#     # get single information
#     QUERY = f"""
# 		SELECT DISTINCT sensor_name, sensor_type
# 		FROM sensors
# 		WHERE sensor_id = {sensor_id}
#     """
#     cursor.execute(QUERY)
#     returned = cursor.fetchall()[0]

#     dict["sensor_name"] = returned[0]
#     dict["sensor_type"] = returned[1]

#     # get multi information
#     QUERY = f"""
# 		SELECT value_type, unit, count
# 		FROM sensors
# 		WHERE sensor_id = {sensor_id}
#     """
#     cursor.execute(QUERY)
#     returned = cursor.fetchall()
    
    
#     dict["value_infos"] = [{"value_type": data["value_type"], "unit": data["unit"], "count": data["count"]} for data in returned]
    
#     # close connector
#     conn.close()

#     return dict


# confirmed
def create_sensor_dict(measurement, network_name, network_strength, 
                       sensor_type, location_name, location_id,
                       sensor_name, sensor_id):
    from datetime import datetime

    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")

    sensor_dict = {
        "date": nowdate,
        "time": nowtime,
        "location": {"id": location_id, "name": location_name},
        "sensor": {"id": sensor_id, "name": sensor_name, "type": sensor_type},
        "measurement": measurement,
        "network": {"name": network_name, "dB": network_strength}
    }

    return sensor_dict



def send_curl(headers, status, url=None):
    import requests

    dict = status["dict"]
    print(dict)

    # POST 요청 보내기
    if url != None:
        response = requests.post(url, json=dict, headers=headers)

        # 응답 확인
        print("Response status code:", response.status_code)
        print("Response body:", response.json())


def send_alert(headers, status, url=None):
    import sqlite3
    import os
    import requests

    # get params
    nowdate = status["dict"]["location_id"]
    nowtime = status["dict"]["location_id"]
    sensor_id = status["dict"]["location_id"]
    sensor_name = status["dict"]["location_id"]
    sensor_type = status["dict"]["location_id"]
    location_id = status["dict"]["location_id"]
    location_name = status["dict"]["location_name"]
    measurement = status["dict"]["measurement"]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_dir = os.path.join(current_dir, f'../../database/sensor.db')

    # open connector
    conn = sqlite3.connect(database_dir)
    cursor = conn.cursor()

    for data in measurement:
        # get params
        value_type = data["value_type"]
        value = data["value"]

        # get values
        QUERY = f"""
        SELECT type_id, type_name, grade
        FROM grade
		WHERE location_id = {location_id}
		AND value_type = {value_type}
		AND {value} BETWEEN bottom_value and top_value
        """
        cursor.execute(QUERY)
        returned = cursor.fetchall()[0]
        type_id = returned[0]
        type_name = returned[1]
        grade = returned[2]

        if grade != "normal":
            data = {
                "date": nowdate,
                "time": nowtime,
                "location": {"id": location_id, "name": location_name},
                "type": {"id": type_id, "name": type_name},
                "grade": grade,
                "data": {
                    "sensor": {"id": sensor_id, "name": sensor_name, "type": sensor_type},
                    "measurement": {"type": value_type, "value":value}
                }
            }

            print(data)

            # POST 요청 보내기
            if url != None:
                response = requests.post(url, json=data, headers=headers)

                # 응답 확인
                print("Response status code:", response.status_code)
                print("Response body:", response.json())

    # close connector
    conn.close()


def send_alert_camera(headers, status, url=None):
    import sqlite3
    import os
    import requests

    # get params
    nowdate = status["dict"]["location_id"]
    nowtime = status["dict"]["location_id"]
    sensor_id = status["dict"]["location_id"]
    sensor_name = status["dict"]["location_id"]
    sensor_type = status["dict"]["location_id"]
    location_id = status["dict"]["location_id"]
    location_name = status["dict"]["location_name"]
    measurement = status["dict"]["measurement"]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_dir = os.path.join(current_dir, f'../../database/sensor.db')

    # open connector
    conn = sqlite3.connect(database_dir)
    cursor = conn.cursor()

    for data in measurement:
        # get params
        value_type = data["value_type"]
        value = data["value"]

        # get values
        QUERY = f"""
        SELECT type_id, type_name, grade
        FROM grade
		WHERE location_id = {location_id}
		AND value_type = {value_type}
		AND {value} BETWEEN bottom_value and top_value
        """
        cursor.execute(QUERY)
        returned = cursor.fetchall()[0]
        type_id = returned[0]
        type_name = returned[1]
        grade = returned[2]

        if grade != "normal":
            data = {
                "date": nowdate,
                "time": nowtime,
                "location": {"id": location_id, "name": location_name},
                "type": {"id": type_id, "name": type_name},
                "grade": grade,
                "data": {
                    "sensor": {"id": sensor_id, "name": sensor_name, "type": sensor_type},
                    "measurement": {"type": value_type, "value":value}
                }
            }

            print(data)

            # POST 요청 보내기
            if url != None:
                response = requests.post(url, json=data, headers=headers)

                # 응답 확인
                print("Response status code:", response.status_code)
                print("Response body:", response.json())

    # close connector
    conn.close()