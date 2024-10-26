from Window import Window
from Geometry import *
from Cell import *

win = Window(800, 600)

cell1 = Cell(700, 750, 400, 425, win)
cell1.draw()
cell2 = Cell(100, 205, 100, 205, win)
cell2.walls["top"] = False
cell2.walls["right"] = False
cell2.draw()
cell1.draw_move(cell2, True)

win.wait_for_close()