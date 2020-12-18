from tkinter import *

root =Tk()

def printname(event):
    print("hello")



button_1 = Button(root, text='Hello')
button_1.bind("<Button-1>", printname)
#"<Button-1>" is for left button
button_1.pack()

root.mainloop()

