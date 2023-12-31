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

    def drawLine(self, line, fillColour="mediumpurple"):
        line.draw(self.__canvas, fillColour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2, width=2) -> None:
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
        self.width = width

    def draw(self, canvas, fillColour):
        canvas.create_line(self.x1, self.y1, 
                           self.x2, self.y2, 
                           fill=fillColour, width=self.width)
        canvas.pack(fill=BOTH, expand=1)