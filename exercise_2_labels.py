from tkinter import *

#label = an area widget that hold text and/or an image within a window
window = Tk()
window.geometry("1200x1200")
window.config(background="black")
photo = PhotoImage(file='panda_logo.png')
label = Label(window,  #note: the first argument here is which container contains this widget
              text="Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='#4DA1E8', 
              bg='#E0FBFF',
              relief=RAISED,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound='bottom') # Display label
label.pack()
#label.place(x=0, y=0) change the position of label (comment the label.pack() command line)

window.mainloop()