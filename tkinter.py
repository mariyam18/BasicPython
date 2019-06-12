from Tkinter import *
win=Tk()
#adding editText field
s1=Entry(win)
s2=Entry(win)
#implementing add,sub, multi and div functions
def add():
	c=int(s1.get())+int(s2.get())
	label.config(text="Addition=%d"%c)
def sub():
	c=int(s1.get())-int(s2.get())
	label.config(text="Substraction=%d"%c)
def multi():
	c=int(s1.get())*int(s2.get())
	label.config(text="Multiplication=%d"%c)
def div():
	c=int(s1.get())/int(s2.get())
	label.config(text="Division=%d"%c)
#adding buttons
b1=Button(win, text='+',command=add)
b2=Button(win, text='-',command=sub)
b3=Button(win, text='*',command=multi)
b4=Button(win, text='/',command=div)
#adding label
label=Label(win,text='answer will be displayed here')
#packing all components
s1.pack()
s2.pack()
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
label.pack(side=RIGHT)
mainloop()
