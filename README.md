# sensor-generator
sensor-generator 레포지토리는 팀 '한울'에서 설계한 데이터 관리 파이프라인의 일부분입니다. 이 레포에서는 산업 환경에서 센서가 측정한 데이터를 json 형태로 가공하여 fastapi_load 레포지토리에서 운영되는 FastAPI 서버로 전송하는 로직을 포함하고 있습니다. 각 센서는 측정된 데이터를 전송 전 자체 검사하여 이상 수치가 관측된 경우 fastapi_alert 레포지토리에서 운영되는 FastAPI 서버로 경보 신호를 전송합니다.

# Usage
1. 센서에서 측정된 데이터의 1차 가공
2. 측정된 데이터를 정해진 주기마다 FastAPI 서버로 데이터 request를 전송
3. 측정된 데이터의 이상치 여부를 확인하고 이상이 있을 경우 FastAPI 서버로 경보 request를 전송

# Structure
### database: SQLite
image

### tree
```
.
├── README.md
├── config
│   └── config.ini
├── database
│   └── sensor.db
├── lib
│   ├── example
│   │   └── gas.py
│   ├── modules
│   │   ├── grade.py
│   │   ├── sensors.py
│   │   └── wifi_information.py
│   └── sensors
│       ├── location_10.py
│       ├── location_11.py
│       ├── location_7.py
│       └── location_8.py
├── sh
│   └── bin
└── src
    └── curl
        ├── location_10
        │   └── send_300.py
        ├── location_11
        │   └── send_400.py
        ├── location_7
        │   ├── send_100.py
        │   └── send_500.py
        └── location_8
            └── send_200.py
```

# Requirements
sensor-generator 레포지토리는 이하의 환경에서 운영되고 있습니다.
### OS
- ubuntu 20.04 LTS
### programs
- python: v3.7.16
### modules
```
pip install -y sqlite3 numpy
```

# Notification
