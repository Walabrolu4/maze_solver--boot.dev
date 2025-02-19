from tkinter import Tk, BOTH, Canvas

class Window():
  def __init__(self,width,height):
    self.width = width
    self.height = height
    self.root = Tk()
    self.root.title = "Maze Solver v0.1"
    self.root.protocol("WM_DELETE_WINDOW",self.close)
    self.canvas = Canvas(self.root,bg="white",width=self.width,height=self.height)
    self.canvas.pack()
    self.running = False
    print("Loading Window class from:", __file__)

  def redraw(self):
    self.root.update_idletasks()
    self.root.update()

  def wait_for_close(self):
    self.running = True
    while self.running:
      self.redraw()

  def close(self):
    self.running = False
  
  def draw_line(self,line,fill_color):
    line.draw(self.canvas,fill_color)
  
  def get_window_size(self):
    self.root.update_idletasks()
    width = self.root.winfo_width()
    height = self.root.winfo_height()
    print(f"height ={height}, width={width}")
    return width,height

  

