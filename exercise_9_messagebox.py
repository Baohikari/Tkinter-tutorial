from tkinter import *
from tkinter import messagebox

def click():
    #Please, remove """ to try some stuffs with messagebox
    #This command show how to make an info messagebox
    """messagebox.showinfo(title='This is an info message box',
                        message='You are a person')"""
    #Warning message
    """messagebox.showwarning(title='WARNING',
                           message='VIRUS DETECTED')"""
    
    #Error message
    """messagebox.showerror(title='ERROR',
                         message='SOMETHING WENT WRONG')"""
    
    #'Ask-ok-cancel' message, it will return true when you OK or false when you CANCEL
    """if messagebox.askokcancel(title='ASK OK CANCLE',
                           message='Do you want to do some stuffs'):
        print("You've done the stuffs")
    else:
        print("You cancelled!!")"""
    
    #'Ask-retry-cancel' message, it's quite same as ask-ok-cancel
    """if messagebox.askretrycancel(title='ASK RETRY CANCEL',
                                 message='DO YOU WANT TO RETRY?'):
        print('You retried')
    else:
        print('You canceled')"""
    
    #'Yes-no' message
    """if messagebox.askyesno(title='Ak yes or no',
                           message='Do you like chocolate cake'):
        print('Everyone loves chocolate cake')
    else:
        print("No one hates chocolate cake, you're joking, right?")"""

    #'ask-question' message
    """answer = messagebox.askquestion(title='Ask question',
                                    message='Do you like pie')
    if answer == 'yes' :
        print('I like pie too')
    else:
        print("WHY DON'T YOU LIKE IT?")"""
    
    # 'ask-yes-no-cancel' message
    # This method will return:
        # True when you click YES
        # False when you click NO
        # None when you click CANCEL
    """anwser = messagebox.askyesnocancel(title='Ask yes no cancel',
                              message='Do you like to code')
    if anwser == True:
        print('I like to code too')
    elif anwser == False:
        print('So, why are you here?!!?')
    else:
        print('Huhhh?')
        """
window = Tk()

button = Button(window,
                command=click,
                text='Click me')
button.pack()
window.mainloop()