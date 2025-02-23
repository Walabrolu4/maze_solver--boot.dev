import unittest
from window import Window
from maze import Maze

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    win = Window(800,600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols,win)
    m1._create_cells()
    self.assertEqual(
        len(m1.cells),
        num_rows,
    )
    self.assertEqual(
        len(m1.cells[0]),
        num_cols,
    )

  def test_maze_reset(self):
    win = Window(800,600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols,win)
    m1._create_cells()
    for row in m1.cells:
      for cell in row:
        cell.visited = True
    self.assertEqual(m1.cells[2][2].visited, True)

    m1._reset_cells_visited()
    self.assertEqual(m1.cells[2][2].visited, False)

if __name__ == "__main__":
  unittest.main()