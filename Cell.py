from Geometry import *

class Cell():
    def __init__(self, x1, x2, y1, y2, win=None):
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if not self._win:
            return None
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.walls["top"]:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.walls["right"]:
            self._win.draw_line(line, "black")
        else: 
            self._win.draw_line(line, "white")
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.walls["bottom"]:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.walls["left"]:
            self._win.draw_line(line, "black")
        else:
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return None
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        center1 = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        center2 = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        between = Point((to_cell._x1 + to_cell._x2)/2, (self._y1 + self._y2)/2)
        line1 = Line(center1, between)
        line2 = Line(between, center2)
        self._win.draw_line(line1, fill_color)
        self._win.draw_line(line2, fill_color)