from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    p2 = Point(10, 590)
    line1 = Line(p1, p2, 4)
    win.drawLine(line1, "mediumpurple")
    win.wait_for_close()

main()