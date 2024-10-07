from tkinter import *
from tkinter import colorchooser #sub-module

def click():
    color = colorchooser.askcolor()
    #print(color) #this will return a tuple: ((R, G, B), Hex value of color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex) #this will change the current background color to colorHex we choose
window = Tk()
window.geometry('420x420')
button = Button(window,
                text='click me',
                command=click)
button.pack()

window.mainloop()