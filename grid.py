import pygame as pg


class Grid:
    def __init__(self):
        # simple lines
        self.gridLines = [((1, 200),  (600, 200)),
                           ((1, 400), (600, 400)),
                           ((200, 1), (200, 600)),
                           ((400, 1), (400, 600))]

    # draw lines of the grid

    def draw(self, surface):
        for line in self.gridLines:
            pg.draw.line(surface, (50, 50, 50), line[0], line[1], 2)
            pg.display.flip()