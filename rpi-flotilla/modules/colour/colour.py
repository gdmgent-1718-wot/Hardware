"""
==============================================
Colour - Flotilla
==============================================
Example with the 'Colour'-module
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
colour = dock.first(flotilla.Colour)

try:
  while True:
    amountOfLight = str(colour.clear)
    amountOfRed = str(colour.red)
    amountOfGreen = str(colour.green)
    amountOfBlue = str(colour.blue)
    print('Waarde van de hoeveelheid licht: ' + amountOfLight)
    print('Waarde van rood in het licht: ' + amountOfRed)
    print('Waarde van groen in het licht: ' + amountOfGreen)
    print('Waarde van blauw in het licht: ' + amountOfBlue)
    time.sleep(10)

except KeyboardInterrupt:
    dock.stop()
