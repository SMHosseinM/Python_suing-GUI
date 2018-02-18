#!/usr/bin/env pyhton
from Tkinter import *

root = Tk()
# bg = background ---> background colour
# fg = frontground ---> frontground colour
one = Label(root, text='One', fg='black', bg='red')
one.pack()

two = Label(root, text='Two', fg='blue', bg='green')
#Fill is used to denote in which directio the 
#Elements should be grow or shrink
two.pack(fill=X)

three = Label(root, text='Three', fg='white', bg='purple')
three.pack(side=LEFT, fill=Y)
root.mainloop()
