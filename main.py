from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    p2 = Point(10, 590)
    line1 = Line(p1, p2)
    win.drawLine(line1, "purple")
    win.wait_for_close()

main()