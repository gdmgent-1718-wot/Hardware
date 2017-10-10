import time
import RPi.GPIO as GPIO

button = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button)

    if input_state == False :
        print(input_state)
        time.sleep(0.5)
