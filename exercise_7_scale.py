from tkinter import *
from PIL import Image, ImageTk
def submit():
    print('The temperature is: ' + str(scale.get()) + ' degree C')
window = Tk()

flame_img = Image.open('flame_icon.png')
flame_img = flame_img.resize((40, 40), Image.Resampling.LANCZOS) #Resize image
flame_img = ImageTk.PhotoImage(flame_img)

flameLabel = Label(image = flame_img)
flameLabel.pack()

scale = Scale(window,
              from_ = 100,
              to = 0,
              length = 600,
              orient = VERTICAL,
              font = ('Consolas', 20),
              tickinterval = 10,        #adds numeric indicators for value
              #showvalue = 0,   #hide current value
              troughcolor = '#2CAFFE',
              fg = '#FF1C00',
              background = 'black') 
scale.set(((scale['from'] - scale['to'])/2) + scale['to'])  #make it to be middle of the cale
scale.pack()

snowflake_img = Image.open('snowflake_icon.png')
snowflake_img = snowflake_img.resize((40, 40), Image.Resampling.LANCZOS) #Resize image
snowflake_img = ImageTk.PhotoImage(snowflake_img)

snowflakeLabel = Label(image = snowflake_img)
snowflakeLabel.pack()

button = Button(window,
                text = "submit",
                command = submit)
button.pack()

window.mainloop()