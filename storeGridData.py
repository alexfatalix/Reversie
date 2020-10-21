import pygame as pg
from drawXO import DrawXO

drawXO = DrawXO()

class StoreGridData:

    def __init__(self):
        self.defaultGrid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.defaultMidPoints = ((100, 100),
                                 (300, 100),
                                 (500, 100),
                                 (100, 300),
                                 (300, 300),
                                 (500, 300),
                                 (100, 500),
                                 (300, 500),
                                 (500, 500))


    def storeXO(self, XO, midPos, surface, thickness, radius, BLUE = (0, 0, 255), RED = (255, 0, 0)):
        numberRect = self.countNumberOfRect(midPos)
        if self.defaultGrid[numberRect - 1] == 0:
            if not XO:
                self.defaultGrid[numberRect - 1] = 1
                print(self.defaultGrid)
            else:
                self.defaultGrid[numberRect - 1] = 2
                print(self.defaultGrid)
        for i in range(0, 9):
            if self.defaultGrid[i] == 1:
                drawXO.drawCross(surface, BLUE, self.defaultMidPoints[i], thickness + 10)
            elif self.defaultGrid[i] == 2:
                drawXO.drawCircle(surface, RED, self.defaultMidPoints[i], radius, thickness)


    def countNumberOfRect(self, midPos):
        counterRect = 0
        temp = 0
        for y in range(0, 600, 200):
            for x in range(0, 600, 200):
                counterRect += 1
                rect = pg.Rect((x, y, x + 200, y + 200))
                if rect.collidepoint(midPos):
                    temp = counterRect
        return temp