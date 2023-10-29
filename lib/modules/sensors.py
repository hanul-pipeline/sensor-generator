
# confirmed
def create_dict_measurement(measurement, network_name, network_strength, 
                       sensor_type, location_name, location_id,
                       sensor_name, sensor_id):
    from datetime import datetime

    # date params
    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")

    # create dict
    dict_measurement = {
        "date": nowdate,
        "time": nowtime,
        "location": {"id": location_id, "name": location_name},
        "sensor": {"id": sensor_id, "name": sensor_name, "type": sensor_type},
        "measurement": measurement,
        "network": {"name": network_name, "dB": network_strength}
    }

    return dict_measurement


# confirmed
def create_dict_alert(dict_measurement, type_id, type_name, grade):
    # copy dict
    dict_alert = dict_measurement

    # input values: type, grade
    dict_alert["type"] = {"id": type_id, "name": type_name}
    dict_alert["grade"] = grade

    return dict_alert


# confirmed
def create_alert(dict_measurement, location_id):
    from grade import grade_single_values, grade_multiple_values

    # create alert
    alert = []

    # define grade
    for data in dict_measurement["measurement"]:
        if data["cnt"] == 1:
            dict_grade = grade_single_values(location_id=location_id,
                                        value_type=data["value_type"],
                                        value=data["value"])
        else:
            dict_grade = grade_multiple_values(location_id=location_id,
                                            value_type=data["value_type"],
                                            value=data["value"],
                                            total_cnt=data["cnt"],
                                            percentage=data["percentage"])
            
        if dict_grade["grade"] != "normal":
            dict_alert = create_dict_alert(dict_measurement=dict_measurement,
                                            type_id=dict_grade["type_id"], 
                                            type_name=dict_grade["type_name"], 
                                            grade= dict_grade["grade"])
            alert.append(dict_alert)
    
    return alert


# confirmed
def send_curl_measurement(headers, status, url=None):
    import requests
    import json

    # get datas
    dict_measurement = status["dict_measurement"]
    print(dict_measurement)

    # change datatype
    # json_measurement = json.dumps(dict_measurement, ensure_ascii=False)
    # print(json_measurement)

    # send POST cURL
    if url != None:
        response = requests.post(url, json=dict_measurement, headers=headers)
        print("Response status code:", response.status_code)


# def send_curl_measurement(headers, status, url=None):
#     import subprocess

#     # get datas
#     dict_measurement = status["dict_measurement"]
#     print(dict_measurement)

#     # change datatype
#     # json_measurement = json.dumps(dict_measurement, ensure_ascii=False)
#     # print(json_measurement)

#     # send POST cURL
#     if url != None:
#         curl_command = f'curl -X POST {url} -H "Content-Type: application/json" -d \'{dict_measurement}\''
#         subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
#         print("SENT")

# confirmed
def send_curl_alert(headers, status, url=None):
    import requests

    # get datas
    alert = status["alert"]
    print("alert:")
    print(alert)

    # send POST cURL
    for dict_alert in alert:
        if url != None:
            response = requests.post(url, json=dict_alert, headers=headers)
            print("Response status code:", response.status_code)
            print("Response body:", response.json())