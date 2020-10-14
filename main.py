import pygame as pg
from grid import Grid
from drawXO import DrawXO
from checkCollides import CheckCollides


# screen stats
WIDTH = 600
HEIGHT = 600

# colors
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# initialize screen
surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("TicTacToe")
clock = pg.time.Clock()
FPS = 60

# init classes
grid = Grid()
drawXO = DrawXO()
checkCollides = CheckCollides()

XO = False

def drawDefaults(midPos, XO):
    surface.fill(WHITE)
    grid.draw(surface)

    if XO == True:
        drawXO.drawCircle(surface, RED, midPos, 75, 10)
    else:
        drawXO.drawCross(surface, BLUE, midPos, 15)


drawDefaults((-1000, -1000), XO)
isRun = True
while isRun:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRun = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                midPos = checkCollides.collideRect(event.pos)
                drawDefaults(midPos, XO)
                XO = not XO




pg.quit()