import pygame as pg
from drawGridData import DrawGridData
from grid import Grid


# screen stats
WIDTH = 600
HEIGHT = 600


# initialize screen
surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("TicTacToe")
clock = pg.time.Clock()
FPS = 60


XO = False
grid = Grid()
drawGridData = DrawGridData()

surface.fill((200, 200, 200))
grid.draw(surface)
isRun = True
while isRun:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRun = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawGridData.drawAll(surface, event.pos, 10, 75, XO)
                pg.display.flip()
                XO = not XO




pg.quit()