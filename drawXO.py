import pygame as pg

pg.init()

class DrawXO:
    def drawCircle(self, surface, color, center, radius, thickness):
        pg.draw.circle(surface, color, center, radius, thickness)
        pg.display.flip()


    def drawCross(self, surface, color, midPoint, thickness):
        startPos1 = (midPoint[0] - 75, midPoint[1] - 75)
        endPos1 = (midPoint[0] + 75, midPoint[1] + 75)
        startPos2 = (midPoint[0] + 75, midPoint[1] - 75)
        endPos2 = (midPoint[0] - 75, midPoint[1] + 75)
        pg.draw.line(surface, color, startPos1, endPos1, thickness)
        pg.draw.line(surface, color, startPos2, endPos2, thickness)
        pg.display.flip()
