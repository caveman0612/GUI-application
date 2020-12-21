from tkinter import *


def doNothing():
    print("Ok I love that...")

root = Tk()

#******** main menu ************

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

#*************** the tool bar *************

toolbar = Frame(root, bg="grey")
insertButt = Button(toolbar, text="cut", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
