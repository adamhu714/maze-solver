from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, bg = 'white', width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
        
    def close(self):
        self.__running = False

    def drawLine(self, line, fillColour):
        line.draw(self.__canvas, fillColour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2) -> None:
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, fillColour):
        canvas.create_line(self.x1, self.y1, 
                           self.x2, self.y2, 
                           fill=fillColour, width=2)