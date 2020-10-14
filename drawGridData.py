from storeGridData import StoreGridData
from drawXO import DrawXO
from checkCollides import CheckCollides
from grid import Grid

storeGridData = StoreGridData()
drawXO = DrawXO()
checkCollides = CheckCollides()
grid = Grid()

# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class DrawGridData:
    def drawAll(self, surface, pointClick, thickness, radius, XO):
        surface.fill((200, 200, 200))
        grid.draw(surface)
        midPoint = checkCollides.collideRect(pointClick)
        storeGridData.storeXO(XO, midPoint)
        for i in range(0, 9):
            if storeGridData.defaultGrid[i] == 1:
                drawXO.drawCross(surface, BLUE, storeGridData.defaultMidPoints[i], thickness+10)
            if storeGridData.defaultGrid[i] == 2:
                drawXO.drawCircle(surface, RED, midPoint, radius, thickness)

