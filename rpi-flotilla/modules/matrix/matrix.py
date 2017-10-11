"""
==============================================
Number - Flotilla
==============================================
Example with the 'Matrix'-module
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

while not dock.ready:
    pass

matrix = dock.first(flotilla.Matrix)


state = True

try:
    while True:
        for module in dock.available.values():
            if module.is_a(flotilla.Matrix):

                #To do? In a for loop :)
                module.set_pixel(3, 0, state).update()
                module.set_pixel(4, 0, state).update()
                
                module.set_pixel(2, 1, state).update()
                module.set_pixel(3, 1, state).update()
                module.set_pixel(4, 1, state).update()
                module.set_pixel(5, 1, state).update()
                
                module.set_pixel(1, 2, state).update()
                module.set_pixel(2, 2, state).update()
                module.set_pixel(3, 2, state).update()
                module.set_pixel(4, 2, state).update()
                module.set_pixel(5, 2, state).update()
                module.set_pixel(6, 2, state).update()

                module.set_pixel(0, 3, state).update()
                module.set_pixel(1, 3, state).update()
                module.set_pixel(2, 3, state).update()
                module.set_pixel(3, 3, state).update()
                module.set_pixel(4, 3, state).update()
                module.set_pixel(5, 3, state).update()
                module.set_pixel(6, 3, state).update()
                module.set_pixel(7, 3, state).update()

                module.set_pixel(0, 4, state).update()
                module.set_pixel(1, 4, state).update()
                module.set_pixel(2, 4, state).update()
                module.set_pixel(3, 4, state).update()
                module.set_pixel(4, 4, state).update()
                module.set_pixel(5, 4, state).update()
                module.set_pixel(6, 4, state).update()
                module.set_pixel(7, 4, state).update()

                module.set_pixel(0, 5, state).update()
                module.set_pixel(1, 5, state).update()
                module.set_pixel(2, 5, state).update()
                module.set_pixel(3, 5, state).update()
                module.set_pixel(4, 5, state).update()
                module.set_pixel(5, 5, state).update()
                module.set_pixel(6, 5, state).update()
                module.set_pixel(7, 5, state).update()

                module.set_pixel(1, 6, state).update()
                module.set_pixel(2, 6, state).update()
                module.set_pixel(5, 6, state).update()
                module.set_pixel(6, 6, state).update()
                
                time.sleep(1)
                module.clear()
                
                module.set_pixel(2, 0, state).update()
                module.set_pixel(3, 0, state).update()
                module.set_pixel(4, 0, state).update()
                module.set_pixel(5, 0, state).update()
                module.set_pixel(6, 0, state).update()
                module.set_pixel(7, 0, state).update()

                module.set_pixel(1, 1, state).update()
                module.set_pixel(2, 1, state).update()
                module.set_pixel(3, 1, state).update()
                module.set_pixel(4, 1, state).update()
                module.set_pixel(5, 1, state).update()
                module.set_pixel(6, 1, state).update()
                module.set_pixel(7, 1, state).update()

                module.set_pixel(0, 2, state).update()
                module.set_pixel(1, 2, state).update()
                module.set_pixel(2, 2, state).update()
                module.set_pixel(3, 2, state).update()
                module.set_pixel(4, 2, state).update()
                module.set_pixel(5, 2, state).update()
                module.set_pixel(6, 2, state).update()
                module.set_pixel(7, 2, state).update()
                module.set_pixel(8, 2, state).update()

                module.set_pixel(0, 3, state).update()
                module.set_pixel(1, 3, state).update()
                module.set_pixel(2, 3, state).update()
                module.set_pixel(5, 3, state).update()
                module.set_pixel(6, 3, state).update()
                module.set_pixel(7, 3, state).update()
                module.set_pixel(8, 3, state).update()

                module.set_pixel(0, 4, state).update()
                module.set_pixel(1, 4, state).update()
                module.set_pixel(2, 4, state).update()
                module.set_pixel(5, 4, state).update()
                module.set_pixel(6, 4, state).update()
                module.set_pixel(7, 4, state).update()
                module.set_pixel(8, 4, state).update()

                module.set_pixel(0, 5, state).update()
                module.set_pixel(1, 5, state).update()
                module.set_pixel(2, 5, state).update()
                module.set_pixel(3, 5, state).update()
                module.set_pixel(4, 5, state).update()
                module.set_pixel(5, 5, state).update()
                module.set_pixel(6, 5, state).update()
                module.set_pixel(7, 5, state).update()
                module.set_pixel(8, 5, state).update()


                module.set_pixel(1, 6, state).update()
                module.set_pixel(2, 6, state).update()
                module.set_pixel(3, 6, state).update()
                module.set_pixel(4, 6, state).update()
                module.set_pixel(5, 6, state).update()
                module.set_pixel(6, 6, state).update()
                module.set_pixel(7, 6, state).update()

                module.set_pixel(2, 7, state).update()
                module.set_pixel(3, 7, state).update()
                module.set_pixel(4, 7, state).update()
                module.set_pixel(5, 7, state).update()
                module.set_pixel(6, 7, state).update()

                time.sleep(1)
                module.clear()

        state = not state

except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
