from point import Point
from line import Line
class Cell():
  def __init__(self,win,has_left_wall,has_right_wall,has_top_wall,has_bottom_wall):
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall

    self._x1 = 0
    self._x2 = 0
    self._y1 = 0
    self._y2 = 0

    self.point_top_left = Point(0,0)
    self.point_top_right = Point(0,0)
    self.point_bottom_left = Point(0,0)
    self.point_bottom_right = Point(0,0)
    self._win = win

  def draw(self,top_left,bottom_right):
    self._x1 = top_left.x
    self._y1 = top_left.y
    self._x2 = bottom_right.x
    self._y2 = bottom_right.y
    self.point_top_left.set(self._x1,self._y1)
    self.point_top_right.set(self._x2,self._y1)
    self.point_bottom_left.set(self._x1,self._y2)
    self.point_bottom_right.set(self._x2,self._y2)

    if self.has_top_wall:
      self._win.draw_line(Line(self.point_top_left,self.point_top_right),"black")
    if self.has_bottom_wall:
      self._win.draw_line(Line(self.point_bottom_left,self.point_bottom_right),"black")
    if self.has_left_wall:
      self._win.draw_line(Line(self.point_top_left,self.point_bottom_left),"black")
    if self.has_right_wall:
      self._win.draw_line(Line(self.point_top_right,self.point_bottom_right),"black")
