"""
==============================================
Dial - Flotilla
==============================================
Example with the 'Dial'-module
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
dial = dock.first(flotilla.Dial)

try:
  while True:
    pos = int(dial.position)
    if pos > 512:
    	print("Luid")
    if 0 < pos < 512:
    	print("Stil")
    time.sleep(1)

except KeyboardInterrupt:
    dock.stop()
