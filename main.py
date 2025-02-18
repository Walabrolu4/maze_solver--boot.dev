from window import Window
from point import Point
from line import Line
from cell import Cell
def Main():
  win = Window(800,600)
  win.canvas.configure(width=800, height=600)


  point = Point(40,40)
  point2 = Point(60,60)

  point3 = Point(90,90)
  point4 = Point(110,110)

  line = Line(point,point2)
  line2 = Line(point3,point4)

  point5 = Point(1,1)
  point6 = Point(10,10)

  
  cell = Cell(win,True,True,True,True)
  cell2 = Cell(win,True,True,False,True)
  cell3 = Cell(win,True,True,True,False)

  win.draw_line(line,"red")
  win.draw_line(line2,"blue")
  cell.draw(point5,point6)
  cell2.draw(point,point2)
  cell3.draw(point3,point4)
  win.wait_for_close()


Main()
