from window import Window
from drawing import Point, Line, Cell
from maze import Maze
import time

color_maze = "black"
color_solver = "blue"

def main():
    my_window = Window(1400, 1000)
    
    p1 = Point(20, 20)
    
    my_maze = Maze(p1.x, p1.y, 14, 24, 50, 50, win=my_window, seed=0)
    my_maze.break_entrance_and_exit()
    my_maze._break_walls_r(0,0)
    my_maze._reset_cells_visited()
    my_maze.solve(0,0)

    my_window.wait_for_close()





if __name__ == '__main__':
    main()