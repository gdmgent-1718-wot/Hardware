import flotilla
import time

dock = flotilla.Client()
slider = dock.first(flotilla.Slider)

try:
  while True:
    pos = int(slider.position)
    if pos > 512:
	    print("Veel!")
    if 0 < pos < 512:
	    print("Weinig!")
    time.sleep(1)

except KeyboardInterrupt:
    dock.stop()
