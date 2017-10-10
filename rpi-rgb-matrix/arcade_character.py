"""
==============================================
RPI 
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
from math import floor, ceil
import time

class ArcadeGenerator(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ArcadeGenerator, self).__init__(*args, **kwargs)

    def drawMatrix(self, canvas, n, xstart, ystart):
        pattern = ""
        rd = randint(0, 255)
        bl = randint(0, 255)
        gr = randint(0, 255)
            
        for r in range(0,n):
            temp = ""
            for c in range(0, int(ceil(n/2))):
                temp = temp + str(int(round(random())))

            reversedTemp = temp[::-1]
            
            if n % 2 != 0:
                reversedTemp = temp[::-1][1:]

            temp = temp + reversedTemp
            pattern = pattern + temp
                
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

        while True:
            self.drawMatrix(offset_canvas, 16, 0, 0)
            self.drawMatrix(offset_canvas, 16, 16, 0)
            self.drawMatrix(offset_canvas, 16, 16, 16)
            self.drawMatrix(offset_canvas, 16, 0, 16)
            
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            time.sleep(5)

# Main function
if __name__ == "__main__":
    arcade_generator = ArcadeGenerator()
    if (not arcade_generator.process()):
        arcade_generator.print_help()
