from cell import Cell
from point import Point
import time
class Maze():
  def __init__(self,x1,y1,num_rows,num_cols,win):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self._win = win
    self.screen_width, self.screen_height = win.get_window_size()
    self.cell_size = min((self.screen_height/num_rows), (self.screen_width/num_cols))
    print(self.cell_size)
    self.cells = list()

  def _create_cells(self):
    for i in range(0,self.num_rows):
      row = []
      for j in range(0,self.num_cols):
        row.append(Cell(self._win))
      self.cells.append(row)

    for i in range(0,self.num_rows):
      for j in range(0,self.num_cols):
        self._draw_cell(i,j)
  
  def _draw_cell(self,i,j):
    point_top_left = Point((j*self.cell_size) + self.x1,(i*self.cell_size) + self.y1)
    point_bottom_right = Point((j*self.cell_size) + self.x1 + self.cell_size,(i*self.cell_size) + self.y1 + self.cell_size)
    self.cells[i][j].draw(point_top_left,point_bottom_right)
  
  def _animate(self):
    self._win.redraw()
    time.sleep(0.5)