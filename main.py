from window import Window
from point import Point
from line import Line

def Main():
  win = Window(800,600)
  win.canvas.configure(width=800, height=600)


  point = Point(1,1)
  point2 = Point(500,500)

  point3 = Point(800,1)
  point4 = Point(1,300)

  line = Line(point,point2)
  line2 = Line(point3,point4)

  win.draw_line(line,"red")
  win.draw_line(line2,"blue")

  win.wait_for_close()


Main()
