
def create_sensor_data(measurement, network_name, network_strength, 
                       type_name, type_id, location_name, location_id,
                       sensor_name, sensor_id, unit):
    from datetime import datetime

    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")

    dict = {
        "type" : {"name" : type_name, "id" : type_id},
        "nowdate": nowdate,
        "nowtime": nowtime,
        "location": {"name": location_name, "id": location_id},
        "type": {"name": type_name, "id": type_id},
        "data": {
            "sensor": {"name": sensor_name, "id": sensor_id},
            "measurement": measurement,
            "unit": unit,
        },
        "connection": {"network_name": network_name, "signal_strength_db": network_strength}
    }

    return dict


def send_curl(url, headers, status):
    import requests

    nowdate = status["dict"]["nowdate"]
    nowtime = status["dict"]["nowtime"]
    loc_nm = status["dict"]["location"]["name"]
    loc_id = status["dict"]["location"]["id"]
    type_nm = status["dict"]["type"]["name"]
    type_id = status["dict"]["type"]["id"]
    sensor_nm = status["dict"]["data"]["sensor"]["name"]
    sensor_id = status["dict"]["data"]["sensor"]["id"]
    measurement = status["dict"]["data"]["measurement"]
    unit = status["dict"]["data"]["unit"]
    network_nm = status["dict"]["connection"]["network_name"]
    network_str = status["dict"]["connection"]["signal_strength_db"]

    data = {
        "날짜": nowdate,
        "시간": nowtime,
        "위치": (loc_nm, loc_id),
        "분류": (type_nm, type_id),
        "데이터": {
            "센서": (sensor_nm, sensor_id),
            "측정값": measurement,
            "단위": unit
        },
        "연결": {
            "네트워크명": network_nm,
            "신호강도(dB)": network_str
        }
    }

    print(data)

    # # POST 요청 보내기
    # response = requests.post(url, json=data, headers=headers)

    # # 응답 확인
    # print("Response status code:", response.status_code)
    # print("Response body:", response.json())

    ##  ok   ok              ok    ok
    ## 위치 센서 분류 등급 측정값 단위


def send_alert(url, headers, status):
    import sqlite3

    nowdate = status["dict"]["nowdate"]
    nowtime = status["dict"]["nowtime"]
    loc_nm = status["dict"]["location"]["name"]
    loc_id = status["dict"]["location"]["id"]
    type_nm = status["dict"]["type"]["name"]
    type_id = status["dict"]["type"]["id"]
    sensor_nm = status["dict"]["data"]["sensor"]["name"]
    sensor_id = status["dict"]["data"]["sensor"]["id"]
    measurement = status["dict"]["data"]["measurement"]
    unit = status["dict"]["data"]["unit"]

    conn = sqlite3.connect('directory')
    cursor = conn.cursor()
    QUERY = f"SELECT type_id, rank FROM rank WHERE {measurement} BETWEEN scope_min and scope_max"
    cursor.execute(QUERY)
    returned = cursor.fetchall()

    type_id = returned[0][0]
    rank = returned[0][1]
    
    data = {
        "날짜": nowdate,
        "시간": nowtime,
        "위치": (loc_nm, loc_id),
        "분류": (type_nm, type_id),
        "등급": rank,
        "데이터": {
            "센서": (sensor_nm, sensor_id),
            "측정값": measurement,
            "단위": unit
        }
    }

    print(data)

    # # POST 요청 보내기
    # response = requests.post(url, json=data, headers=headers)

    # # 응답 확인
    # print("Response status code:", response.status_code)
    # print("Response body:", response.json())

    ##  ok   ok              ok    ok