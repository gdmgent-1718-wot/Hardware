from picamera import PiCamera
from os import system

camera = PiCamera()

for i in range(10):
        camera.capture('image{0:04}.jpg'.format(i))

#install imagemagic
# ==> sudo apt-get install imagemagick -y

#convert images to gif with
# ==> convert -delay 10 -loop 0 image*.jpg animation.gif

system('convert -delay 10 -loop 0 image*.jpg animation.gif')
print('done')

        
