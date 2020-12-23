from tkinter import *

from tkinter import ttk
import tkinter.messagebox

class atm:
  def __init__(self, root):
    self.root = root
    self.root.title("ATM system")
    self.root.geometry("774x760+280+0")
    self.root.configure(bg='gainsboro')

if __name__=='__main__':
  root = Tk()
  application = atm(root)
  root.mainloop()