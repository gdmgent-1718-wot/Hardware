"""
==============================================
Motion - Flotilla
==============================================
Example with the 'Motion'-module
----------------------------------------------
Course:     Web Of Things (WOT)
Option:     New Media Development
Department: Graphic and Digital Media
College:    Artevelde University College Ghent
----------------------------------------------
Authors:
    - Ismail Kutlu
    - Niels Cappelle
==============================================
"""


import time

import flotilla

dock = flotilla.Client()
motion = dock.first(flotilla.Motion)

MOTION_INFO = "x={x}, y={y}, z={z}"

try:
    while True:
        print(MOTION_INFO.format(
            x=motion.x,
            y=motion.y,
            z=motion.z))
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
