import time
import RPi.GPIO as GPIO
from Adafruit_BME280 import *

led_output = 27

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_output, GPIO.OUT)

led = False

while True:
    degrees = sensor.read_temperature()
    print('Temp = ' + str(round(degrees)) + ' C')

    if degrees >= 20 :
        led = True
    else :
        led = False

    GPIO.output(led_output, led)
    
    time.sleep(0.5)
