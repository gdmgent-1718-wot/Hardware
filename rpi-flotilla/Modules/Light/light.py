import flotilla
import time

dock = flotilla.Client()
light = dock.first(flotilla.Light)

try:
  while True:
    calculation = light.light
    lightlevel = str(calculation)
    print("Het lichtniveau bedraagt " + lightlevel)
    time.sleep(3)

except KeyboardInterrupt:
  dock.stop()
