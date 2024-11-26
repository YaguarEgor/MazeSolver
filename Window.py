from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.__canvas = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        
    def redraw(self):
        self.__root_widget.update()
        self.__root_widget.update_idletasks()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
        
        