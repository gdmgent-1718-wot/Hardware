"""
==============================================
Motor - Flotilla
==============================================
Example with the 'Motor'-module
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
import sys

import flotilla

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
motor = dock.first(flotilla.Motor)

if motor is None:
    print("Some modules required were not found...")
    print("Make sure you have a Motor and a Touch module attached to the Dock!")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")

# Starts the loop going so it keeps working until we stop it
try:
    while True:
        motor.set_speed(100)
        motor.update()
        time.sleep(1)
        motor.stop()
        time.sleep(1)



# This listens for a keyboard interrupt, which is Ctrl+C and can stop the program
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
