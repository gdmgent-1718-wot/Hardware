"""
==============================================
Touch - Flotilla
==============================================
Example with the 'Touch'-module
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

dock = flotilla.Client()
touch = dock.first(flotilla.Touch)

try:
    while True:
        if touch.one:
            print("Knop 1 is ingedrukt!")
        if touch.two:
            print("Knop 2 is ingedrukt!")
        if touch.three:
            print("Knop 3 is ingedrukt!")
        if touch.four:
            print("Knop 4 is ingedrukt!")

except KeyboardInterrupt:
    dock.stop()
