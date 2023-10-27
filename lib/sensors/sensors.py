
def create_sensor_data(measurement, network_name, network_strength, 
                       sensor_type, location_name, location_id,
                       sensor_name, sensor_id, unit, type_id, type_name):
    from datetime import datetime

    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")

    dict = {
        "nowdate": nowdate,
        "nowtime": nowtime,
        "location_name": location_name,
        "location_id": location_id,
        "sensor_type": sensor_type,
        "sensor_name": sensor_name,
        "sensor_id": sensor_id,
        "measurement": measurement,
        "unit": unit,
        "network_name": network_name, 
        "signal_strength_db": network_strength,
        "type_id": type_id,
        "type_name": type_name
    }

    return dict


def send_curl(headers, status, url=None):
    import requests

    nowdate = status["dict"]["nowdate"]
    nowtime = status["dict"]["nowtime"]
    loc_nm = status["dict"]["location_name"]
    loc_id = status["dict"]["location_id"]
    sensor_type = status["dict"]["sensor_type"]
    sensor_nm = status["dict"]["sensor_name"]
    sensor_id = status["dict"]["sensor_id"]
    measurement = status["dict"]["measurement"]
    unit = status["dict"]["unit"]
    network_nm = status["dict"]["network_name"]
    network_str = status["dict"]["signal_strength_db"]

    data = {
        "date": nowdate,
        "time": nowtime,
        "location": {"id": loc_nm, "name": loc_id},
        "type_name": sensor_type,
        "sensor": {"id": sensor_id, "name": sensor_nm, "type": sensor_type},
        "measurement": {"value": measurement, "unit": unit},
        "network": {"name": network_nm, "dB": network_str}
    }

    print(data)

    # POST 요청 보내기
    if url != None:
        response = requests.post(url, json=data, headers=headers)

        # 응답 확인
        print("Response status code:", response.status_code)
        print("Response body:", response.json())


def send_alert(headers, status, url=None):
    import sqlite3

    nowdate = status["dict"]["nowdate"]
    nowtime = status["dict"]["nowtime"]
    location_nm = status["dict"]["location_name"]
    location_id = status["dict"]["location_id"]
    type_id = status["dict"]["type_id"]
    type_nm = status["dict"]["type_name"]
    sensor_type = status["dict"]["sensor_type"]
    sensor_nm = status["dict"]["sensor_name"]
    sensor_id = status["dict"]["sensor_id"]
    measurement = status["dict"]["measurement"]
    unit = status["dict"]["unit"]

    if sensor_type == "열화상카메라":
        pass
    else:
        for key, value in measurement.items():
            conn = sqlite3.connect('directory')
            cursor = conn.cursor()
            QUERY = f"""SELECT grade 
                        FROM grade
                        WHERE location_id = {location_id}
                        AND type_id = {type_id}
                        AND {measurement} BETWEEN scope_min AND scope_max"""
            cursor.execute(QUERY)
            returned = cursor.fetchall()
            rank = returned[0][0]
    
    rank = "rank"

    data = {
        "date": nowdate,
        "time": nowtime,
        "location": {"id": location_nm, "name": location_id},
        "type": {"id": type_id, "name": type_nm},
        "rank": rank,
        "data": {
            "sensor": {"id": sensor_id, "name": sensor_nm, "type": sensor_type},
            "measurement": {"value": measurement, "unit": unit},
        }
    }

    print(data)

    # POST 요청 보내기
    if url != None:
        response = requests.post(url, json=data, headers=headers)

        # 응답 확인
        print("Response status code:", response.status_code)
        print("Response body:", response.json())