import time
import RPi.GPIO as GPIO

led_output = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_output, GPIO.OUT)

led = False

while True:
    led = not led
    GPIO.output(led_output, led_blauw)
    time.sleep(0.5)
