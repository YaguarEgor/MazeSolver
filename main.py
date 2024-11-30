from Maze import Maze
from Window import Window


if __name__ == "__main__":
    num_rows = 5
    num_cols = 5
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols 
    cell_size_y = (screen_y - 2 * margin) / num_rows 
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    input()