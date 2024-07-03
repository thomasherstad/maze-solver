class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=4
            )


class Cell:
    def __init__(self, win, x_top_left, y_top_left, x_bot_right, y_bot_right):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x_top_left
        self._x2 = x_bot_right
        self._y1 = y_top_left
        self._y2 = y_bot_right
        self._win = win

    def draw(self, color):
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1),(Point(self._x1, self._y2)))
            left_wall.draw(self._win.canvas, color)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1),(Point(self._x2, self._y2)))
            right_wall.draw(self._win.canvas, color)
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1),(Point(self._x2, self._y1)))
            top_wall.draw(self._win.canvas, color)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2),(Point(self._x2, self._y2)))
            bottom_wall.draw(self._win.canvas, color)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        x_center = (self._x1 + self._x2)/2
        y_center = (self._y1 + self._y2)/2
        x_to_cell_center = (to_cell._x1 + to_cell._x2)/2
        y_to_cell_center = (to_cell._y1 + to_cell._y2)/2

        line = Line(Point(x_center, y_center), Point(x_to_cell_center, y_to_cell_center))
        line.draw(self._win, color)