from tkinter import *
def hello(event):
    print("Single Click, Button-l") 
def Cool(event):                           
    print("That's cool!")

widget = Button(None, text='Hello!')
widget.pack()
widget.bind('<Button-1>', hello)
widget.mainloop()

widget = Button(None, text='Cool!')
widget.pack()
widget.bind('<Double-1>', Cool)
