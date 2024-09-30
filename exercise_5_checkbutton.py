from tkinter import *

def display():
    if x.get():
        print('You agreed!!')
    else:
        print("You didn't agree")
window = Tk()

x = BooleanVar()

python_photo = PhotoImage(file = 'python_logo.png')

check_button = Checkbutton(window,
                           text = 'I agree to something',
                           variable = x,
                           onvalue = True,
                           offvalue = False,
                           command = display,
                           font = ('Arial', 20),
                           fg = '#2CAFFE',
                           bg = 'white',
                           activeforeground = '#2CAFFE',
                           activebackground = 'white',
                           padx = 25,
                           pady = 10,
                           image = python_photo,
                           compound = 'left')
check_button.pack()

window.mainloop()