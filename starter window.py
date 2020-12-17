from tkinter import *

root =Tk()

one = Label(root, text="one thing", bg="red", fg="white")
one.pack()

two = Label(root, text="another thing", bg="blue", fg="black")
two.pack(fill=X)

three = Label(root, text="same thing", bg="yellow", fg="black")
three.pack(side=LEFT, fill=Y)

root.mainloop()