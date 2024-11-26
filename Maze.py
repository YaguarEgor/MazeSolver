from Geometry import *
from Cell import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            self._cells.append([])
            for j in range(self._num_cols):
                self._cells[i].append(
                    Cell(self._x1+j*self._cell_size_x, self._x1+(j+1)*self._cell_size_x,
                                 self._y1+i*self._cell_size_y, self._y1+(i+1)*self._cell_size_y, self._win))
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        
        
                
    def _draw_cell(self, i, j):
        if not self._win:
            return None
        self._cells[i][j].draw()
        self._animate()
        
    def _animate(self):
        if not self._win:
            return None
        self._win.redraw()
        time.sleep(0.02)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].walls["left"] = False
        self._cells[0][0].draw()
        self._animate()
        self._cells[self._num_rows-1][self._num_cols-1].walls["right"] = False
        self._cells[self._num_rows-1][self._num_cols-1].draw()
        self._animate()
    