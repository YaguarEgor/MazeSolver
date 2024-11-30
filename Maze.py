from Geometry import *
from Cell import *
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
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
        
        
        
                
    def _draw_cell(self, i, j):
        if not self._win:
            return None
        self._cells[i][j].draw()
        self._animate()
        
    def _animate(self):
        if not self._win:
            return None
        self._win.redraw()
        time.sleep(0.1)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].walls["left"] = False
        self._cells[0][0].draw()
        self._animate()
        self._cells[self._num_rows-1][self._num_cols-1].walls["right"] = False
        self._cells[self._num_rows-1][self._num_cols-1].draw()
        self._animate()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and self._cells[i - 1][j]._visited == False:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_rows - 1 and False == self._cells[i + 1][j]._visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and False == self._cells[i][j - 1]._visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_cols - 1 and False == self._cells[i][j + 1]._visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].walls["right"] = False
                self._cells[i + 1][j].walls["left"] = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].walls["left"] = False
                self._cells[i - 1][j].walls["right"] = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].walls["bottom"] = False
                self._cells[i][j + 1].walls["top"] = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].walls["top"] = False
                self._cells[i][j - 1].walls["bottom"] = False
            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
        return
    
    
    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j._visited = False
    
    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].walls["left"]
            and not self._cells[i - 1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_rows- 1
            and not self._cells[i][j].walls["right"]
            and not self._cells[i + 1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].walls["top"]
            and not self._cells[i][j - 1]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_cols - 1
            and not self._cells[i][j].walls["bottom"]
            and not self._cells[i][j + 1]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False

    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)        