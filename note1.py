#!/usr/bin/env python
from Tkinter import *

# This one is just making a plane window
# You can consider it as a equivalent to 
# getPaineContainer() class in java
# The entire exression is important 
# It plays as a template for u
root = Tk()

# In order to add text to the Tinker we need to use
# Label function which the first argumet asks where
# You want to put ur label and the second one is 
# What is ur label
#theLabel = Label(root, text="This is too easy")

# In python whatever GUI function u use you
# need to make is ready to be displayed
# This one is as the same as pack function in java
#theLabel.pack()

# When you have gui application, you need that 
# Continuously on the screen until you decide to 
# close it down(pressin the x). this purpose can 
# be achieved using the following function.
# root is the plain window
#root.mainloop()

#Frame is similar to the borderlayout in java
#Enabling you to partioning your window and 
#Use diferent widget for each of them.
#The argument says where you want use this frame
topFrame = Frame(root)

#Whenever we want something display on the screen
#We pack it. Same thing applies to Frame
topFrame.pack()

#Let's here add another Frame and put it at the 
#Bottom of window
bottomFrame = Frame(root)

#Side expression as the pack argument says
#Where you want to leave this fram
bottomFrame.pack(side=BOTTOM)

#Now let's add some botton to our window
#In order to that that we can use a function 
#Called: Button(x, y, z)
#It takes 3 paramete. 
#First one says which Frame shuld this button resides
#Second one says what kind of text should be displayed
#On the button
#third on is optional and is for changing the colour of text
button1 = Button(topFrame, text='Button 1', fg='red')
button2 = Button(topFrame, text='Button 2', fg='green')
button3 = Button(topFrame, text='Button 3', fg='blue')
button4 = Button(bottomFrame, text='Button 4', fg='purple')

button1.pack(side=LEFT);
button2.pack(side=LEFT);
button3.pack(side=LEFT);
button4.pack();
root.mainloop();
