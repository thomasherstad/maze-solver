from drawing import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.seed = random.seed(seed)
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
        time.sleep(0.01)
    
    def break_entrance_and_exit(self):
        if self._cells is None:
            return
        start_cell = self._cells[0][0]
        start_cell.has_top_wall = False
        self._draw_cell(start_cell)

        end_cell = self._cells[self._num_cols-1][self._num_rows-1]
        end_cell.has_bottom_wall = False
        self._draw_cell(end_cell)
    

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = []
            #Check the cells that are directly adjacent to the current cell. Keep track of any that have not been visited as "possible directions" to move to
            above_neighbor = (i,j-1)
            below_neighbor = (i,j+1)
            right_neighbor = (i+1,j)
            left_neighbor = (i-1,j)
            neighbors = [above_neighbor, below_neighbor, right_neighbor, left_neighbor]
            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                if neighbor[0] >= self._num_cols or neighbor[1] >= self._num_rows:
                    continue
                if not self._cells[neighbor[0]][neighbor[1]].visited:
                    possible_directions.append(neighbor)
            #If there are zero directions you can go from the current cell, then draw the current cell and return to break out of the loop
            if len(possible_directions) == 0:
                current_cell.draw("black")
                break
            #Otherwise, pick a random direction.
            else:
                chosen_cell = random.choice(possible_directions)
            #Knock down the walls between the current cell and the chosen cell.
            if chosen_cell == above_neighbor:
                current_cell.has_top_wall = False
                current_cell.draw("black")
                above_cell = self._cells[above_neighbor[0]][above_neighbor[1]]
                above_cell.has_bottom_wall = False
                above_cell.draw("black")

            elif chosen_cell == below_neighbor:
                current_cell.has_bottom_wall = False
                current_cell.draw("black")
                below_cell = self._cells[below_neighbor[0]][below_neighbor[1]]
                below_cell.has_top_wall = False
                below_cell.draw("black")          

            elif chosen_cell == right_neighbor:
                current_cell.has_right_wall = False
                current_cell.draw("black")
                right_cell = self._cells[right_neighbor[0]][right_neighbor[1]]
                right_cell.has_left_wall = False
                right_cell.draw("black")

            elif chosen_cell == left_neighbor:
                current_cell.has_left_wall = False
                current_cell.draw("black")
                left_cell = self._cells[left_neighbor[0]][left_neighbor[1]]
                left_cell.has_right_wall = False
                left_cell.draw("black")
            #Move to the chosen cell by recursively calling _break_walls_r
            self._break_walls_r(chosen_cell[0], chosen_cell[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    

    def solve(self, i, j):
        return self._solve_r(i,j)
        
    #The _solve_r method returns True if the current cell is an end cell, OR if it leads to the end cell. It returns False if the current cell is a loser cell.
    def _solve_r(self, i, j):
        current_cell = self._cells[i][j]
        #Call the _animate method.
        self._animate()
        #Mark the current cell as visited
        current_cell.visited = True
        #If you are at the "end" cell (the goal) then return True.
        end_cell_pos = (self._num_cols-1, self._num_rows-1)
        if (i, j) == end_cell_pos:
            return True
        elif (i, j) == end_cell_pos:
            return True
        
        #Find directions without walls
        #directions = right, left, bottom, top
        directions = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        walls = [current_cell.has_right_wall, current_cell.has_left_wall, current_cell.has_bottom_wall, current_cell.has_top_wall]
        allowed_directions = []
        for i in range(len(directions)):
            if walls[i] != True:
                allowed_directions.append(directions[i])

        for direction in allowed_directions:
            if direction[0] >= 0 and direction[1] >= 0 and direction[0] < self._num_cols and direction[1] < self._num_rows:
                to_cell = self._cells[direction[0]][direction[1]]
                if to_cell.visited == False: #CHECK FOR NO WALL
                    current_cell.draw_move(to_cell)
                    if self._solve_r(direction[0], direction[1]):
                        return True
                    else:
                        current_cell.draw_move(to_cell, undo=True)
        return False