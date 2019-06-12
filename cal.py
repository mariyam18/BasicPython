from Tkinter import *

win=Tk()


s1=Entry(win)
s2=Entry(win)

def add():
	c=int(s1.get())+int(s2.get())
	label.config(text="Adition=%d"%c)
	
def sub1():
	c=int(s1.get())-int(s2.get())
	label.config(text="substraction=%d"%c)
	
b1=Button(win,text='+',command=add)
b2=Button(win,text='-',command=sub1)
label=Label(win,text='Answer')

s1.pack()
s2.pack()
b1.pack()
b2.pack(side=LEFT)
label.pack()

mainloop()
