from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

#note: all the widgets are created and used between Tk() and mainloop()
window = Tk() # instantiate an instance of a window
window.geometry("420x420") #change the size of window ("widthxheight")
window.title("Tkinter tutorial") #Change title of window


icon = PhotoImage(file='panda_logo.png')
window.iconphoto(True, icon) #change the icon of window

window.config(background="#E0FBFF")


window.mainloop() #place window on computer screen, listen for events

