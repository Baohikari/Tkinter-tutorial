from tkinter import *
from PIL import Image, ImageTk #Use this library to handle image
#radio button = similar to checkbox, but you can only select one from a group
food = ['pizza', 'hamburger', 'hotdog']

def order():
    if x.get() == 0:
        print('You ordered pizza')
    elif x.get() == 1:
        print("You ordered hamburger")
    elif x.get() == 2:
        print("Your ordered hot dog")
    else:
        print("Huh??")
window = Tk()

x = IntVar()

pizza_img = Image.open('pizza_icon.png')
pizza_img = pizza_img.resize((50, 50), Image.Resampling.LANCZOS) #Resize image
pizza_img = ImageTk.PhotoImage(pizza_img) #Convert to PhotoImage

hotdog_img = Image.open('hotdog_icon.png')
hotdog_img = hotdog_img.resize((50, 50), Image.Resampling.LANCZOS) #Resize image
hotdog_img = ImageTk.PhotoImage(hotdog_img) #Convert to PhotoImage

hamburger_img = Image.open('hamburger_icon.png')
hamburger_img = hamburger_img.resize((50, 50), Image.Resampling.LANCZOS) #Resize image
hamburger_img = ImageTk.PhotoImage(hamburger_img) #Convert to PhotoImage


foodImages = [pizza_img, hamburger_img, hotdog_img]

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text = food[index], # adds text to radio buttons
                               variable = x,       # groups radiobutton together if they share the same variable
                               value = index,      # assigns each radiobutton a different value
                               padx = 25,
                               font = ('Impact', 50),
                               image = foodImages[index], # adds image to radiobuttons
                               compound = 'left',
                               indicatoron = 0,    # eliminate circle indicators
                               width = 375,        # set width radiobuttons
                               command = order)    # set command of radiobutton to function    
          
    radio_button.pack(anchor = 'w')

window.mainloop()