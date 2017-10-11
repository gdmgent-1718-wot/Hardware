import flotilla
import time

dock = flotilla.Client()
joystick = dock.first(flotilla.Joystick)

try:
  while True:
    print("You are holding the joystick at coordinates ({0}, {1})".format(joystick.x, joystick.y))
    time.sleep(.5)

except KeyboardInterrupt:
  dock.stop()
