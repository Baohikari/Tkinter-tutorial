from tkinter import *

#list box = a listing of selectable text items within its own container
def sizing_list_box():
    listbox.config(height = listbox.size())
def submit():
    """food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))"""


    print("You have ordered: ")
    print(listbox.get(listbox.curselection()))

    """for index in food:
        print(index)"""

def add():
    listbox.insert(listbox.size(), entryBox.get())
    sizing_list_box()

def delete():
    """for index in reversed(listbox.curselection()):
        listbox.delete(index)"""

    listbox.delete(listbox.curselection())
    sizing_list_box()
window = Tk()

listbox = Listbox(window,
                  bg = "#f7ffde",
                  font = ("Constantia", 35),
                  width = 12,
                  #selectmode=MULTIPLE
                  )
                  #if there is selectmode = MULTIPLE, there's problem occurs!!!
listbox.pack()


listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

entryBox = Entry(window)
entryBox.pack()

addBtn = Button(window,
text="Add",
command=add)
addBtn.pack()

deleteBtn = Button(window,
text="Delete",
command=delete)
deleteBtn.pack()

submitBtn = Button(window,
text = "Submit",
command=submit)
submitBtn.pack()

sizing_list_box()
window.mainloop()