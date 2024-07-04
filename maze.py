from drawing import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                x_top_left = self._x1 + self._cell_size_x*i
                y_top_left = self._y1 + self._cell_size_y*j
                x_bot_right = x_top_left + self._cell_size_x
                y_bot_right = y_top_left + self._cell_size_y
                cell = Cell(x_top_left, y_top_left, x_bot_right, y_bot_right, self._win)
                col.append(cell)
                if self._win is not None:
                    self._draw_cell(cell)
            self._cells.append(col)

    def _draw_cell(self, cell):
        cell.draw("black")
        self._animate()
        
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def break_entrance_and_exit(self):
        if self._cells is None:
            return
        start_cell = self._cells[0][0]
        start_cell.has_top_wall = False
        self._draw_cell(start_cell)

        end_cell = self._cells[self._num_cols-1][self._num_rows-1]
        end_cell.has_bottom_wall = False
        self._draw_cell(end_cell)