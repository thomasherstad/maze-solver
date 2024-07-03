from window import Window
from drawing import Point, Line

def main():
    my_window = Window(1200, 800)
    
    p1 = Point(20, 20)
    p2 = Point(400, 400)
    line = Line(p1, p2)
    my_window.draw_line(line, "red")

    line2 = Line(Point(400,400), Point(400, 20))
    my_window.draw_line(line2, "blue")

    my_window.wait_for_close()





if __name__ == '__main__':
    main()