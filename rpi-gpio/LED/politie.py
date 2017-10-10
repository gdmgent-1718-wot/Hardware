import time
import RPi.GPIO as GPIO

led_blauw_output = 18
led_rood_output = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_blauw_output, GPIO.OUT)
GPIO.setup(led_rood_output, GPIO.OUT)

led_blauw = False
led_rood = True

while True:
    led_blauw = not led_blauw
    led_rood = not led_rood
    GPIO.output(led_blauw_output, led_blauw)
    GPIO.output(led_rood_output, led_rood)
    time.sleep(0.5)
