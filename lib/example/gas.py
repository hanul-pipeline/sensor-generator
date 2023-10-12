
def sensor_404():
    import RPi.GPIO as GPIO
    import time

    start_time = time.time()

    GPIO.setmode(GPIO.BCM)
    is_running=True
    GPIO.setup(23,GPIO.IN) # 센서 입력
    GPIO.setup(25,GPIO.OUT) # LED

    try:
        while is_running:
            if GPIO.input(23)==1:
                GPIO.output(25,GPIO.HIGH) #LED ON
                print("on")
                return ("1")
            else :
                GPIO.output(25,GPIO.LOW) #LED OFF
                print("off")
                return("0")

    except KeyboardInterrupt:
        GPIO.cleanup()
        is_running=False
    
    end_time = time.time()
    time.sleep(1-(end_time-start_time))