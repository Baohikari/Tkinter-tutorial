from tkinter import *
# button = you click it, then it does stuff
def click():
    print("You clicked me!!")
window = Tk()
window.geometry('520x520')
photo = PhotoImage(file = 'heart_img.png')

button = Button(window,
                text = 'Click me!',
                command = click,
                font=('Comic Sans', 30),
                fg="#FF9205",
                bg="black",
                activeforeground="#FFF2D4",
                activebackground="white",
                state = ACTIVE,
                image = photo,
                compound='right') #display buttons
button.pack()

window.mainloop()