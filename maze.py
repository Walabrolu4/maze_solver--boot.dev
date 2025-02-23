from cell import Cell
from point import Point
import time
import random
class Maze():
  def __init__(self,x1,y1,num_rows,num_cols,win,*,seed=None):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self._win = win
    self.screen_width, self.screen_height = win.get_window_size()
    self.cell_size = 20#min((self.screen_height/num_rows), (self.screen_width/num_cols))
    print(self.cell_size)
    self.cells = list()
    if seed:
      random.seed(seed)

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
    time.sleep(0.1)

  def _break_entrance_and_exit(self):
    self.cells[0][0].has_top_wall = False
    self.cells[-1][-1].has_bottom_wall = False
    
    self._draw_cell(0, 0)  # entrance
    self._draw_cell(self.num_rows-1, self.num_cols-1)  # exit

  def _break_walls_r(self,i,j):
    self.cells[i][j].visited = True
    while True:
      to_visit = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
      to_visit = list(filter(lambda index: self.is_valid(index),to_visit))
      if not to_visit:
        break
      choice = random.choice(to_visit)

      if choice == (i+1, j):  # Move down
          self.cells[i][j].has_bottom_wall = False
          self.cells[i+1][j].has_top_wall = False
          self._draw_cell(i, j)
          self._draw_cell(i+1, j)

      elif choice == (i-1, j):  # Move up
          self.cells[i][j].has_top_wall = False
          self.cells[i-1][j].has_bottom_wall = False
          self._draw_cell(i, j)
          self._draw_cell(i-1, j)

      elif choice == (i, j+1):  # Move right
          self.cells[i][j].has_right_wall = False
          self.cells[i][j+1].has_left_wall = False
          self._draw_cell(i, j)
          self._draw_cell(i, j+1)

      elif choice == (i, j-1):  # Move left
          self.cells[i][j].has_left_wall = False
          self.cells[i][j-1].has_right_wall = False
          self._draw_cell(i, j)
          self._draw_cell(i, j-1)

      self._break_walls_r(choice[0],choice[1])
  
  def _reset_cells_visited(self):
    for row in self.cells:
      for cell in row:
        cell.visited = False
  
  def is_valid(self,index):
    r, c = index
    rows = len(self.cells)
    cols = len(self.cells[0])
    return 0 <= r < rows and 0 <= c < cols and not self.cells[index[0]][index[1]].visited
  
  def solve(self):
    return self._solve_r(0,0)
  

  def _solve_r(self,i,j):
    self._animate()
    self.cells[i][j].visited = True
    if i == len(self.cells)-1 and j == len(self.cells[i])-1:
      return True
    
    #(i+1, j):  # Move down
    if self.is_valid((i+1,j)) and not self.cells[i+1][j].has_top_wall:
      self.cells[i][j].draw_move(self.cells[i+1][j])
      if self._solve_r(i+1,j):
        return True
      else:
        self.cells[i][j].draw_move(self.cells[i+1][j],undo=True)

    #(i-1, j):  # Move up
    if self.is_valid((i-1,j)) and not self.cells[i-1][j].has_bottom_wall:
      self.cells[i][j].draw_move(self.cells[i-1][j])
      if self._solve_r(i-1,j):
        return True
      else:
        self.cells[i][j].draw_move(self.cells[i-1][j],undo=True)

    #(i, j+1):  # Move right
    if self.is_valid((i,j+1)) and not self.cells[i][j+1].has_left_wall:
      self.cells[i][j].draw_move(self.cells[i][j+1])
      if self._solve_r(i,j+1):
        return True
      else:
        self.cells[i][j].draw_move(self.cells[i][j+1],undo=True)

    #(i, j-1):  # Move left
    if self.is_valid((i,j-1)) and not self.cells[i][j-1].has_right_wall:
      self.cells[i][j].draw_move(self.cells[i][j-1])
      if self._solve_r(i,j-1):
        return True
      else:
        self.cells[i][j].draw_move(self.cells[i][j-1],undo=True)

    return False
      

    
