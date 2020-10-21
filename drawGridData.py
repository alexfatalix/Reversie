from storeGridData import StoreGridData
from checkCollides import CheckCollides
from grid import Grid

storeGridData = StoreGridData()
checkCollides = CheckCollides()
grid = Grid()


class DrawGridData:
    def drawAll(self, surface, pointClick, thickness, radius, XO):
        surface.fill((200, 200, 200))
        grid.draw(surface)
        midPoint = checkCollides.collideRect(pointClick)
        storeGridData.storeXO(XO, midPoint, surface, thickness, radius)

