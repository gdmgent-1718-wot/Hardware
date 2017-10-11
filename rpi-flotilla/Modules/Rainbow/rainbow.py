import flotilla
import time

dock = flotilla.Client()
rainbow = dock.first(flotilla.Rainbow)

try:
  while True:
    rainbow.set_pixel(0, 255, 0, 0)
    rainbow.update()
    time.sleep(1)
    rainbow.set_pixel(1, 255, 0, 0)
    rainbow.update()
    time.sleep(1)
    rainbow.set_pixel(2, 255, 0, 0)
    rainbow.update()
    time.sleep(1)
    rainbow.set_pixel(3, 255, 0, 0)
    rainbow.update()
    time.sleep(1)
    rainbow.set_pixel(4, 255, 0, 0)
    rainbow.update()
    time.sleep(1)
    rainbow.set_all(0, 255, 0)
    rainbow.update()
    time.sleep(1)

except KeyboardInterrupt:
    dock.stop()
