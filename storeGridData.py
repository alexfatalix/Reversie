import pygame as pg


class StoreGridData:

    def __init__(self):
        self. defaultGrid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.defaultMidPoints = ((100, 100),
                                 (300, 100),
                                 (500, 100),
                                 (100, 300),
                                 (300, 300),
                                 (500, 300),
                                 (100, 500),
                                 (300, 500),
                                 (500, 500))

    def storeXO(self, XO, midPos):
        numberRect = self.countNumberOfRect(midPos)
        if XO == False:
            self.defaultGrid[numberRect - 1] = 1
        else:
            self.defaultGrid[numberRect - 1] = 2

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

