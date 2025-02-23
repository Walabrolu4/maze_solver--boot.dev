from point import Point
from line import Line
class Cell():
  def __init__(self,win,has_left_wall=True, has_right_wall=True, has_top_wall =True, has_bottom_wall=True):
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self.visited = False
    self.x1 = 0
    self.y1 = 0
    self.x2 = 0
    self.y2 = 0

    self.center = Point(0,0)

    self.point_top_left = Point(0,0)
    self.point_top_right = Point(0,0)
    self.point_bottom_left = Point(0,0)
    self.point_bottom_right = Point(0,0)
    self._win = win

  def draw(self,top_left,bottom_right):
    self.x1 = top_left.x
    self.y1 = top_left.y
    self.x2 = bottom_right.x
    self.y2 = bottom_right.y
    self.point_top_left.set(self.x1,self.y1)
    self.point_top_right.set(self.x2,self.y1)
    self.point_bottom_left.set(self.x1,self.y2)
    self.point_bottom_right.set(self.x2,self.y2)

    if self.has_top_wall:
      self._win.draw_line(Line(self.point_top_left,self.point_top_right),"black")
    else:
      self._win.draw_line(Line(self.point_top_left,self.point_top_right),"white")
    if self.has_bottom_wall:
      self._win.draw_line(Line(self.point_bottom_left,self.point_bottom_right),"black")
    else:
      self._win.draw_line(Line(self.point_bottom_left,self.point_bottom_right),"white")
    if self.has_left_wall:
      self._win.draw_line(Line(self.point_top_left,self.point_bottom_left),"black")
    else:
      self._win.draw_line(Line(self.point_top_left,self.point_bottom_left),"white")    
    if self.has_right_wall:
      self._win.draw_line(Line(self.point_top_right,self.point_bottom_right),"black")
    else:
      self._win.draw_line(Line(self.point_top_right,self.point_bottom_right),"white")    
  
  def draw_move(self,to_cell,undo=False):
    line = Line(self.get_center(),to_cell.get_center())
    if undo:
      self._win.draw_line(line,"grey")
    else:
      self._win.draw_line(line,"red")

  def get_center(self):
    return Point((self.x1+self.x2)/2 , (self.y1+self.y2)/2)

