#!/usr/bin/env python
from Tkinter import *

root = Tk()

label_1 = Label(root, text='name')
label_2 = Label(root, text='family')

# Entry is a function like label in java
# Enable you to interact with gui
entry_1 = Entry(root)
entry_2 = Entry(root)

# grid is the same java grid enable you
# to find the location you want to leave 
# the widgets
# Sticky enable us to say in which location of 
# The grid the text must be displayed
# It takes N E S W 
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

# Adding check box is as follow
# The value stored in the check box variable is either 
# True or False
c = Checkbutton(root, text='Keep me logged in')
# It merge 2 columns to form a one and 
# then put the text in the middle of them
c.grid(columnspan=2)

root.mainloop()
