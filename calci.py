
from Tkinter import *
win = Tk()

s1=Entry(win)
s2=Entry(win)
def add():
	c=int(s1.get())+int(s2.get())
	label.config(text="Addition=%d"%c)

def substract():
	c=int(s1.get())-int(s2.get())
	label.config(text="Substraction=%d"%c)
	
def multiply():
	c=int(s1.get())*int(s2.get())
	label.config(text="Multiplication=%d"%c)
	
def divide():
	c=int(s1.get())/int(s2.get())
	label.config(text="Division=%d"%c)
	
b=Button(win,text='+',command=add)
b1=Button(win,text='-',command=substract)
b2=Button(win,text='*',command=multiply)
b3=Button(win,text='/',command=divide)
label=Label(win,text="Answer")
s1.pack()
s2.pack()
b.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
label.pack()
mainloop()
