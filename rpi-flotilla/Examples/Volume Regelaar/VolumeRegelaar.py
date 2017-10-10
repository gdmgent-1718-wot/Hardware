import flotilla
import time
import math

dock = flotilla.Client()
dial = dock.first(flotilla.Dial)
rainbow = dock.first(flotilla.Rainbow)

if dial is None:
    print("no Dial module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Dial module found. Running...")

if rainbow is None:
    print("no Rainbow module found...")
    dock.stop()
    sys.exit(1)
else:
    print("Rainbow module found. Running...")


try:
    while True:
        pos = int(dial.position)

        if  800 < pos:
            print("Te luid!")
            rainbow.set_all(255, 0, 0)
            rainbow.update()
        if 600 < pos <= 800:
            print("Luid")
            rainbow.set_pixel(4, 0, 255, 0)
            for x in range (0 , 4):
                rainbow.set_pixel(x, 255, 0, 0)
                rainbow.update()
        if 400 < pos <= 600:
            print("Normaal")
            for x in range (3 , 4):
                rainbow.set_pixel(x, 0, 255, 0)
                rainbow.update()
            for x in range (0 , 3):
                rainbow.set_pixel(x, 255, 0, 0)
                rainbow.update()
        if 200 < pos <= 400:
            print("Stil")
            for x in range (2 , 4):
                rainbow.set_pixel(x, 0, 255, 0)
                rainbow.update()
            for x in range (0 , 2):
                rainbow.set_pixel(x, 255, 0, 0)
                rainbow.update()
        if 1 <= pos <= 200:
            print("Heel stil")
            for x in range (1 , 4):
                rainbow.set_pixel(x, 0, 255, 0)
                rainbow.update()
            rainbow.set_pixel(0, 255, 0, 0)
            rainbow.update()
        if 0 >= pos:
            print("Niets")
            rainbow.set_all(0, 255, 0)
            rainbow.update()
        volumeCalculation = math.ceil(pos/100)
        volume = str(volumeCalculation)
        print("Volume: " + volume)
        rainbow.update()
        time.sleep(2)
except KeyboardInterrupt:
    dock.stop()
