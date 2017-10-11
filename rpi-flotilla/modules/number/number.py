"""
==============================================
Motion - Flotilla
==============================================
Example with the 'Number'-module
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
number = dock.first(flotilla.Number)
clock = int(time.strftime('%H%M'))


try:
    while True:
        print(clock)
        number.set_number(clock)
        number.update()
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
