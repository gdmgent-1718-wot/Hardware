"""
==============================================
NFC
==============================================
Course:     Web Of Things (WOT)
Option:     New Media Development
Department: Graphic and Digital Media
College:    Artevelde University College Ghent
----------------------------------------------
Authors:
    - Philippe De Pauw - Waterschoot
----------------------------------------------
Resources:
    - https://github.com/svvitale/nxppy
==============================================
"""

# Python wrapper for interfacing with the NXP EXPLORE-NFC shield for Raspberry Pi
import nxppy
import os, sys, time

print('Application started.')

# Create Mifare Object
mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        
        try:
            uid = mifare.select()
            print('Detected NFC Tag UID: %r' %uid)

        except nxppy.SelectError:
            # SelectError is raised if no card is in the field.
            pass

        time.sleep(1)
        
    except (KeyboardInterrupt, SystemExit):
        print('Application closed.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

