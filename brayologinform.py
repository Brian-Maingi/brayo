from tkinter import*
#import os
from tkinter import messagebox

class LoginPage:#Creates a class window to hold all items
    def __init__(self, master):
        self.master = master
        master.title("Login page")
        global  e1
        global  e2
        global  root

    def label(self):
       lb=Label(root,text='username')
       lc=Label(root,text='password')
       lb.grid(row=1,column=1)
       lc.grid(row=2,column=1)

    def entry(self):
        self.e1=Entry(root)
        self.e1.grid(row=1,column=2)
        self.e2 =Entry(root,show='x')
        self.e2.grid(row=2,column=2)
    def clear1(self):
        self.e1.delete(0,END)

    def regbutton(self):
        bt2 = Button(root, text='cancel',
                     command=root.destroy)
        bt2.grid(row=5, column=3)

        bt1=Button(root,text='register',
                  command=self.register)
        bt1.grid(row=4, column=2)
        bt3=Button(root,text='x',
                   command=self.clear1())
        bt3.grid(row=4, column=1)
    def register(self):
         #file=open('yoo','w') you linked this code block  with the bryan file or password file.
         #file.write(self.e1.get())
         #file.write('\n')
         #file.write(self.e2.get())
         #file.close()
        messagebox.showinfo(('sucessifully signed up!'))






root=Tk()
my_gui = LoginPage(root)
my_gui.label()
my_gui.entry()
my_gui.regbutton()
my_gui.register()
root.mainloop()
