#!/usr/bin/bin/ env python

from Tkinter import *

root = Tk()


#def printName():
#	print("My name is Mohammad Hossein")

##command property defines what kind of behaviour the 
##key must show after being clicked.
##bear in mind whenever u use it, you should have ()
##after the function name
#button_1 = Button(root, text='click me', command=printName)
#button_1.pack()

#Another way

# We we want to call a function based on an event we pass event
# as an argument to the function
def printName(event):
	print("My name is Hossein")

button_1 = Button(root, text='click me')

# .bind enable us to bind one widget to another one
# .bind takes 2 parameters.
# the first one is the kind of the action 
# the second one is what function should be called
# the event for right click is <Button-1>
# Whenever you call a function you must not put the ()
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
