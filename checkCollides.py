import pygame as pg


class CheckCollides:
    @staticmethod
    def collideRect(pointClick):              # this func find rect by click coords and return mid point of it
        counterRect = 0
        for y in range(0, 600, 200):
            for x in range(0, 600, 200):
                counterRect += 1
                rect = pg.Rect((x, y, x + 200, y + 200))
                if rect.collidepoint(pointClick):
                    temp = [x, y]

        temp[0] += 100
        temp[1] += 100
        return temp


