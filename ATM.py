from tkinter import *

from tkinter import ttk
import tkinter.messagebox

class atm:
  def __init__(self, root):
    self.root = root
    self.root.title("ATM System")
    self.root.geometry("774x760+280+0")
    self.root.configure(bg='gainsboro')

    MainFrame = Frame(self.root, bd=10, width=774, height=760, relief=RIDGE)
    MainFrame.grid()

    TopFrame1 = Frame(MainFrame, bd=3, width=724, height=400, relief=RIDGE)
    TopFrame1.grid(row = 1, column = 0, padx = 12)

    TopFrame2 = Frame(MainFrame, bd=3, width=724, height=300, relief=RIDGE)
    TopFrame2.grid(row = 0, column = 0, padx = 8)

    TopFrame2Left = Frame(MainFrame, bd=1, width=300, height=300, relief=RIDGE)
    TopFrame2Left.grid(row = 0, column = 0, padx = 8)

    TopFrame2Mid = Frame(MainFrame, bd=1, width=100, height=300, relief=RIDGE)
    TopFrame2Mid.grid(row = 0, column = 1, padx = 8)

    TopFrame2Right = Frame(MainFrame, bd=1, width=300, height=300, relief=RIDGE)
    TopFrame2Right.grid(row = 0, column = 2, padx = 8)

if __name__=='__main__':
  root = Tk()
  application = atm(root)
  root.mainloop()