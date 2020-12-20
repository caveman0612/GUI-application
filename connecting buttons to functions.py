from tkinter import *


def doNothing():
    print("Ok I love that...")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Now project", command=doNothing)
subMenu.add_command(label="Now ...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=Frame.quit)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="do nothing", command=doNothing)


root.mainloop()
