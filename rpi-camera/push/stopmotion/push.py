from sense_hat import SenseHat
from time import sleep
from picamera import PiCamera
from os import system

#sensehat instantie aanmaken
sensehat = SenseHat()

#camera instantie aanmaken
camera = PiCamera()
camera.resolution = (300,300)
camera.start_preview()

#joystick event voor stopmotion
# instalatie libav-tools -> voor gebruik avconv command voor renereren van stop-motion film
# ==> sudo apt-get libav-tools
while True:
    try:
        sensehat.stick.wait_for_event()
        for i in range(10):
            camera.capture('image{0:04}.jpg'.format(i))
        camera.stop_preview()
        system('avconv -r 10 -r animation/frame%03d.jpg -qscale 2 animation.mp4')
        print('done')
        break
    except KeyboardInterrupt:
        break









