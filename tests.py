import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        
    def test_maze_create_cells_2(self):
        num_cols = 15
        num_rows = 13
        m1 = Maze(0, 0, num_rows, num_cols, 30, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_maze_break_entry_and_exit(self):
        num_cols = 15
        num_rows = 13
        m1 = Maze(0, 0, num_rows, num_cols, 30, 10)
        self.assertEqual(
            m1._cells[0][0].walls["left"],
            False
        )
        self.assertEqual(
            m1._cells[num_rows-1][num_cols-1].walls["bottom"],
            True
        )
        

if __name__ == "__main__":
    unittest.main()