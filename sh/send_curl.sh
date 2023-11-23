#!/bin/bash

# 현재 스크립트 파일의 절대 경로
SH_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# 특정 파일의 절대 경로
CURL_DIR="$SH_DIR/../src/curl"
LOG_DIR="$SH_DIR/../logs/nohup"

# 센서 스크립트 실행하기
nohup python3 $CURL_DIR/location_7/send_100.py >> $LOG_DIR/100.log 2>&1 &
nohup python3 $CURL_DIR/location_8/send_200.py >> $LOG_DIR/200.log 2>&1 &
nohup python3 $CURL_DIR/location_10/send_300.py >> $LOG_DIR/300.log 2>&1 &
nohup python3 $CURL_DIR/location_11/send_400.py >> $LOG_DIR/400.log 2>&1 &
nohup python3 $CURL_DIR/location_7/send_500.py >> $LOG_DIR/500.log 2>&1 &
nohup python3 $CURL_DIR/location_7/send_600.py >> $LOG_DIR/600.log 2>&1 &
