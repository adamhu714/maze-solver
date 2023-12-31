from tkinter import Tk, BOTH, Canvas

# Class for our actual application window
class Window:
    def __init__(self, width, height):
        # Root is the window
        self._root = Tk()
        self._root.title('Maze Solver')
        # Canvas is what we display in the window
        self._canvas = Canvas(self._root, bg = 'white', width=width, height=height)
        # Pack the canvas inside our window
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        # Close the window when we press the close button on the window
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Update the window while the program is running
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")
        
    def close(self):
        self._running = False

    def draw_line(self, line, fill_colour="mediumpurple"):
        line.draw(self._canvas, fill_colour)

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

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.x1, self.y1, 
                           self.x2, self.y2, 
                           fill=fill_colour, width=self.width)
        canvas.pack(fill=BOTH, expand=1)