from Geometry import *

class Cell():
    def __init__(self, x1, x2, y1, y2, win):
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if self.walls["top"]:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.walls["right"]:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.walls["bottom"]:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.walls["left"]:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
    
    def draw_move(self, to_cell, undo=False):
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