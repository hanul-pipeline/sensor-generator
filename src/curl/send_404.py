from my_module import sensor_404
import requests

# URL 및 데이터 설정
url = "http://example.com/api"

# 헤더 설정
headers = {"Content-Type": "application/json"}

for status in sensor_404():
    nowdate = status["nowdate"]
    nowtime = status["nowtime"]
    loc_nm = status["location"]["name"]
    loc_id = status["location"]["id"]
    type_nm = status["type"]["name"]
    type_id = status["type"]["id"]
    sensor_nm = status["data"]["sensor"]["name"]
    sensor_id = status["data"]["sensor"]["id"]
    measurement = status["data"]["measurement"]
    unit = status["data"]["unit"]
    elapsed = status["data"]["elapsed_time_sec"]
    network_nm = status["connection"]["network_name"]
    network_str = status["connection"]["signal_strength_db"]

    data = {
        "날짜": nowdate,
        "시간": nowtime,
        "위치": (loc_nm, loc_id),
        "분류": (type_nm, type_id),
        "데이터": {
            "센서": (sensor_nm, sensor_id),
            "측정값": measurement,
            "단위": unit,
            "경과시간(sec)": elapsed
        },
        "연결": {
            "네트워크명": network_nm,
            "신호강도(dB)": network_str
        }
    }

    # POST 요청 보내기
    response = requests.post(url, json=data, headers=headers)

    # 응답 확인
    print("Response status code:", response.status_code)
    print("Response body:", response.json())
