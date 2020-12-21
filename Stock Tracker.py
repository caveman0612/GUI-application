from tkinter import *

root = Tk()

name_var = StringVar()
passw_var = StringVar()

def submit():
    name = name_entry.get()
    password = passw_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    passw_var.set("")


#creating a label for company and iserting it on page
name_label = Label(root, text="company")
name_label.grid(row=0, column=0)

#company name entry and insert
name_entry = Entry(root, textvariable = name_var)
name_entry.grid(row=0, column=1)

#stock price of company label
passw_label = Label(root, text="stock price")
passw_label.grid(row=1, column=0)

#stock price of company entry
passw_entry = Entry(root, textvariable=passw_var)
passw_entry.grid(row=1, column=1)

#submit button
submit_button = Button(root, text="submit", command=submit)
submit_button.grid(row=2, column=1)

root.mainloop()