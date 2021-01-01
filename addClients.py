from tkinter import *
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('bank.db')
c = conn.cursor()

class AddClients(Toplevel):
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('650x750+550+200')
    self.title('Add Client')
    self.resizable(False, False)

    #Frames
    self.top = Frame(self, height=150, bg='white')
    self.top.pack(fill=X)
    self.bottomFrame = Frame(self, height=500, bg='#118ab2')
    self.bottomFrame.pack(fill=X)

    #heading
    self.heading = Label(self.top, text='Add Clients', bg='white', font='Times 15 bold')
    self.heading.place(x=200, y=60)

    #entries
    #pin
    self.lbl_pin = Label(self.bottomFrame, text="PIN", font='arial 15 bold')
    self.lbl_pin.place(x=40, y=40)
    self.ent_pin = Entry(self.bottomFrame, width=30, bd=4)
    self.ent_pin.insert(0, 'Enter a pin')
    self.ent_pin.place(x=150, y=40)

    #balance
    self.lbl_balance = Label(self.bottomFrame, text="Balance", font='arial 15 bold')
    self.lbl_balance.place(x=40, y=80)
    self.ent_balance = Entry(self.bottomFrame, width=30, bd=4)
    self.ent_balance.insert(0, 'Enter balance')
    self.ent_balance.place(x=150, y=80)

    #submit
    button = Button(self.bottomFrame, text='Add Client', command=self.addClient)
    button.place(x=270, y=140)
  
  def addClient(self):
    o_pin = self.ent_pin.get()
    o_balance = self.ent_balance.get()

    if(len(o_pin) == 3 ):
      try:
        query="INSERT INTO 'clients' (pin,balance) VALUES(?,?)"
        c.execute(query,(o_pin, o_balance))
        conn.commit()
        messagebox.showinfo("Success","Successfully added to database!",icon='info')
      except:
        messagebox.showerror("Error", "Can't add to database!", icon='warning')

    else:
      messagebox.showerror("Error","PIN must be four numbers!",icon='warning')
