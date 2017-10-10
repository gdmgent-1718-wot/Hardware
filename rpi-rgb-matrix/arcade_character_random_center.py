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

# 
from samplebase import SampleBase
from random import random, randint
from math import math, floor, ceil
import time

class ArcadeGenerator(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ArcadeGenerator, self).__init__(*args, **kwargs)

    def drawMatrix(self, canvas, n):
        pattern = ""
        rd = randint(0, 255)
        bl = randint(0, 255)
        gr = randint(0, 255)
            
        for r in range(0,n):
            temp = ""
            for c in range(0, int(floor(n/2))):
                temp = temp + str(int(round(random())))

            temp = temp + temp[::-1]
            pattern = pattern + temp


        xstart = floor((32-n)/2)
        ystart = floor((32-n)/2)
                
        for p in range(0,n*n):
            bit = int(pattern[p])
            r = floor(p/n)
            c = p-n*r            
            
            state = True if bit == 1 else False
            if state == True:
                canvas.SetPixel(c+xstart, r+ystart, rd, gr, bl)
            else:
                canvas.SetPixel(c+xstart, r+ystart, 0, 0, 0) 

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

        while True:
            self.drawMatrix(offset_canvas, a[randint(0, len(a)-1)])
            
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            time.sleep(5)

# Main function
if __name__ == "__main__":
    arcade_generator = ArcadeGenerator()
    if (not arcade_generator.process()):
        arcade_generator.print_help()
