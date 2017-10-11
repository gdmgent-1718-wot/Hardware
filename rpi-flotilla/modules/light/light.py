"""
==============================================
Light - Flotilla
==============================================
Example with the 'Light'-module
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
