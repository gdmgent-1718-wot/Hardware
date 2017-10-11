"""
==============================================
Barometer - Flotilla
==============================================
Example with the 'Barometer'-module
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
weather = dock.first(flotilla.Weather)

try:
  while True:
    temperature = str(weather.temperature)
    print("De temperatuur bedraagt op dit moment " + temperature +'˚C')

    pressure = str(weather.pressure/10)
    print("De luchtdruk bedraagt op dit moment " + pressure +' hPa')
    
    time.sleep(3)

except KeyboardInterrupt:
  dock.stop()
