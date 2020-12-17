from tkinter import *

root =Tk()

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="click here B!", fg="red")
button2 = Button(topframe, text="click here B2", fg="blue")
button3 = Button(topframe, text="click here B3", fg="green")
button4 = Button(bottomframe, text="click here B4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack()
button4.pack()

root.mainloop()

