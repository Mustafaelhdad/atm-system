from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

#create or connect database!!
conn = sqlite3.connect('bank.db')

#create cursor
c = conn.cursor()

#create table
# c.execute("""CREATE TABLE clients (
#   pin integer,
#   balance integer
# )""")

#insert data into the db
c.execute("INSERT INTO clients VALUES (:pin, :balance)"
  {
    'pin': pin.get(),
    'balance': balance.get()
  }
)

#commit changes
conn.commit()

#close db connection
conn.close()

class atm:
  def __init__(self, root):
    self.root = root
    self.root.title("ATM System")
    self.root.geometry("798x760+280+0")
    self.root.configure(bg='gainsboro')

    MainFrame = Frame(self.root, bd=10, width=784, height=700, relief=RIDGE)
    MainFrame.grid()

    TopFrame1 = Frame(MainFrame, bd=3, width=734, height=300, relief=RIDGE)
    TopFrame1.grid(row = 1, column = 0, padx = 12)

    TopFrame2 = Frame(MainFrame, bd=3, width=734, height=300, relief=RIDGE)
    TopFrame2.grid(row = 0, column = 0, padx = 8)

    TopFrame2Left = Frame(TopFrame2, bd=1, width=190, height=300, relief=RIDGE)
    TopFrame2Left.grid(row = 0, column = 0, padx = 8)

    TopFrame2Mid = Frame(TopFrame2, bd=1, width=200, height=300, relief=RIDGE)
    TopFrame2Mid.grid(row = 0, column = 1, padx = 8)

    TopFrame2Right = Frame(TopFrame2, bd=1, width=190, height=300, relief=RIDGE)
    TopFrame2Right.grid(row = 0, column = 2, padx = 8)
    #==============================================================================

    def enter_Pin():
      pinNo = self.txtReceipt.get('1.0', 'end-1c')
      if(pinNo == str('2213') or pinNo == str('4323') or pinNo == str('5982')):
        self.txtReceipt.delete('1.0', END)

        self.txtReceipt.insert(END, '\t\tATM' + '\n\n')
        self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Loan' + '\n\n\n\n')
        self.txtReceipt.insert(END, 'Cash with Receipt\t\t\t Deposit' + '\n\n\n\n')
        self.txtReceipt.insert(END, 'Balance \t\t\t Request New Pin' + '\n\n\n\n')
        self.txtReceipt.insert(END, 'Mini statement\t\t\t Print statement' + '\n\n\n\n')

        self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=loan, image=self.img_arrow_right).grid(row = 0, column = 0, padx = 2, pady = 4)
    
        self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=deposit, image=self.img_arrow_right).grid(row = 1, column = 0, padx = 2, pady = 4)
    
        self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=request_new_pin, image=self.img_arrow_right).grid(row = 2, column = 0, padx = 2, pady = 4)
    
        self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=statement, image=self.img_arrow_right).grid(row = 3, column = 0, padx = 2, pady = 4)

        self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=withdrawcash, image=self.img_arrow_left).grid(row = 0, column = 0, padx = 2, pady = 4)
    
        self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=withdrawcash, image=self.img_arrow_left).grid(row = 1, column = 0, padx = 2, pady = 4)
    
        self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=balance, image=self.img_arrow_left).grid(row = 2, column = 0, padx = 2, pady = 4)
    
        self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=statement, image=self.img_arrow_left).grid(row = 3, column = 0, padx = 2, pady = 4)
      else:
        self.txtReceipt.delete('1.0',END)
        self.txtReceipt.insert(END, 'Invalid Pin Number' + '\n\n')

    def clear():
      self.txtReceipt.delete('1.0',END)
      self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.img_arrow_right).grid(row = 0, column = 0, padx = 2, pady = 4)
    
      self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.img_arrow_right).grid(row = 1, column = 0, padx = 2, pady = 4)
    
      self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.img_arrow_right).grid(row = 2, column = 0, padx = 2, pady = 4)
    
      self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.img_arrow_right).grid(row = 3, column = 0, padx = 2, pady = 4)

      self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=self.img_arrow_left).grid(row = 0, column = 0, padx = 2, pady = 4)
    
      self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=self.img_arrow_left).grid(row = 1, column = 0, padx = 2, pady = 4)
    
      self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=self.img_arrow_left).grid(row = 2, column = 0, padx = 2, pady = 4)
    
      self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=self.img_arrow_left).grid(row = 3, column = 0, padx = 2, pady = 4)

    def insert0():
      value0 = 0
      self.txtReceipt.insert(END, value0)

    def insert1():
      value1 = 1
      self.txtReceipt.insert(END, value1)

    def insert2():
      value2 = 2
      self.txtReceipt.insert(END, value2)

    def insert3():
      value3 = 3
      self.txtReceipt.insert(END, value3)

    def insert4():
      value4 = 4
      self.txtReceipt.insert(END, value4)

    def insert5():
      value5 = 5
      self.txtReceipt.insert(END, value5)

    def insert6():
      value6 = 6
      self.txtReceipt.insert(END, value6)

    def insert7():
      value7 = 7
      self.txtReceipt.insert(END, value7)

    def insert8():
      value8 = 8
      self.txtReceipt.insert(END, value8)

    def insert9():
      value9 = 9
      self.txtReceipt.insert(END, value9)

    def cancel():
      Cancel = tkinter.messagebox.askyesno("ATM", "Do you want to confirm cancel?")
      if Cancel > 0:
        self.root.destroy()
        return

    def withdrawcash():
      enter_Pin()
      self.txtReceipt.delete('1.0',END)
      self.txtReceipt.focus_set()

    def loan():
      enter_Pin()
      self.txtReceipt.delete('1.0',END)
      self.txtReceipt.insert(END, 'Loan $ ')
      self.txtReceipt.focus_set()

    def deposit():
      enter_Pin()
      self.txtReceipt.delete('1.0',END)
      self.txtReceipt.focus_set()

    def request_new_pin():
      enter_Pin()
      self.txtReceipt.delete('1.0', END)
      self.txtReceipt.insert(END, '\t\tWelcome to 7masa Bank\n')
      self.txtReceipt.insert(END, 'New pin number will be send to your email address\n')
      self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Loan' + '\n\n\n\n')
      self.txtReceipt.insert(END, 'Cash with Receipt\t\t\t Deposit' + '\n\n\n\n')
      self.txtReceipt.insert(END, 'Balance \t\t\t Request New Pin' + '\n\n\n\n')
      self.txtReceipt.insert(END, 'Mini statement\t\t\t Print statement' + '\n\n\n\n')
      self.txtReceipt.insert(END, '\t\tThanks for using 7masa Bank\n')

    def balance():
      self.txtReceipt.delete('1.0', END)
      self.txtReceipt.insert(END, '\t\tWelcome to 7masa Bank\n')
      self.txtReceipt.insert(END, '$767' + '\n')
      self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Loan' + '\n\n\n\n')
      self.txtReceipt.insert(END, 'Cash with Receipt\t\t\t Deposit' + '\n\n\n\n')
      self.txtReceipt.insert(END, 'Balance \t\t\t Request New Pin' + '\n\n\n\n')
      self.txtReceipt.insert(END, 'Mini statement\t\t\t Print statement' + '\n\n\n\n')
      self.txtReceipt.insert('1.0', '\t\tThanks for using 7masa Bank\n')

    def statement():
      pinNo1 = str(self.txtReceipt.get('1.0', 'end-1c'))
      pinNo2 = str(pinNo1)
      pinNo3 = float(pinNo2)
      pinNo4 = float(767 - (pinNo3))
      self.txtReceipt.delete('1.0', END)
      self.txtReceipt.insert(END, '\n\t' + str(pinNo4) + '\n')
      self.txtReceipt.insert(END, '\t\t\t\n\n Account Balance $'+ str(pinNo4) + '\t\t\n\n')
      self.txtReceipt.insert(END, 'Rent \t\t\t\t $1000' + '\n\n')

    #==============================================================================
    self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial', 9, 'bold'))
    self.txtReceipt.grid(row = 0, column = 0)
    #==============================================================================

    self.img_arrow_left = PhotoImage(file='icons/lArrow.png')

    self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=withdrawcash, image=self.img_arrow_left).grid(row = 0, column = 0, padx = 2, pady = 4)
    
    self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=withdrawcash, image=self.img_arrow_left).grid(row = 1, column = 0, padx = 2, pady = 4)
    
    self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=balance,image=self.img_arrow_left).grid(row = 2, column = 0, padx = 2, pady = 4)
    
    self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=statement,image=self.img_arrow_left).grid(row = 3, column = 0, padx = 2, pady = 4)
    #==============================================================================

    self.img_arrow_right = PhotoImage(file='icons/rArrow.png')

    self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=loan, image=self.img_arrow_right).grid(row = 0, column = 0, padx = 2, pady = 4)
    
    self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=deposit, image=self.img_arrow_right).grid(row = 1, column = 0, padx = 2, pady = 4)
    
    self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=request_new_pin, image=self.img_arrow_right).grid(row = 2, column = 0, padx = 2, pady = 4)
    
    self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=statement, image=self.img_arrow_right).grid(row = 3, column = 0, padx = 2, pady = 4)
    #==============================================================================

    self.img1 = PhotoImage(file='icons/one.png')
    self.btn1 = Button(TopFrame1, width=160, height=60,command=insert1 , image=self.img1).grid(row = 2, column = 0, padx = 2, pady = 4)
    
    self.img2 = PhotoImage(file='icons/two.png')
    self.btn2 = Button(TopFrame1, width=160, height=60,command=insert2 , image=self.img2).grid(row = 2, column = 1, padx = 2, pady = 4)
    
    self.img3 = PhotoImage(file='icons/three.png')
    self.btn3 = Button(TopFrame1, width=160, height=60,command=insert3 , image=self.img3).grid(row = 2, column = 2, padx = 2, pady = 4)
    
    self.imgCE = PhotoImage(file='icons/cancel.png')
    self.btn3 = Button(TopFrame1, width=160, height=60, command=cancel, image=self.imgCE).grid(row = 2, column = 3, padx = 2, pady = 4)
    
    self.img4 = PhotoImage(file='icons/four.png')
    self.btn4 = Button(TopFrame1, width=160, height=60,command=insert4 , image=self.img4).grid(row = 3, column = 0, padx = 2, pady = 4)

    self.img5 = PhotoImage(file='icons/five.png')
    self.btn5 = Button(TopFrame1, width=160, height=60,command=insert5 , image=self.img5).grid(row = 3, column = 1, padx = 2, pady = 4)
    
    self.img6 = PhotoImage(file='icons/six.png')
    self.btn6 = Button(TopFrame1, width=160, height=60,command=insert6 , image=self.img6).grid(row = 3, column = 2, padx = 2, pady = 4)
    
    self.imgCL = PhotoImage(file='icons/clear.png')
    self.btnCL = Button(TopFrame1, width=160, height=60, command=clear, image=self.imgCL).grid(row = 3, column = 3, padx = 2, pady = 4)
    
    self.img7 = PhotoImage(file='icons/seven.png')
    self.btn7 = Button(TopFrame1, width=160, height=60,command=insert7 , image=self.img7).grid(row = 4, column = 0, padx = 2, pady = 4)

    self.img8 = PhotoImage(file='icons/eight.png')
    self.btn8 = Button(TopFrame1, width=160, height=60,command=insert8 , image=self.img8).grid(row = 4, column = 1, padx = 2, pady = 4)
    
    self.img9 = PhotoImage(file='icons/nine.png')
    self.btn9 = Button(TopFrame1, width=160, height=60,command=insert9 , image=self.img9).grid(row = 4, column = 2, padx = 2, pady = 4)
    
    self.imgEnter = PhotoImage(file='icons/enter.png')
    self.btnEnter = Button(TopFrame1, width=160, height=60, command=enter_Pin, image=self.imgEnter).grid(row = 4, column = 3, padx = 2, pady = 4)
    
    self.imgSp1 = PhotoImage(file='icons/empty.png')
    self.btnSp1 = Button(TopFrame1, width=160, height=60, image=self.imgSp1).grid(row = 5, column = 0, padx = 2, pady = 4)

    self.img0 = PhotoImage(file='icons/zero.png')
    self.btn0 = Button(TopFrame1, width=160, height=60, command=insert0, image=self.img0).grid(row = 5, column = 1, padx = 2, pady = 4)
    
    self.imgSp2 = PhotoImage(file='icons/empty.png')
    self.btnSp2 = Button(TopFrame1, width=160, height=60, image=self.imgSp2).grid(row = 5, column = 2, padx = 2, pady = 4)
    
    self.imgSp3 = PhotoImage(file='icons/empty.png')
    self.btnSp3 = Button(TopFrame1, width=160, height=60, image=self.imgSp3).grid(row = 5, column = 3, padx = 2, pady = 4)


if __name__=='__main__':
  root = Tk()
  application = atm(root)
  root.mainloop()