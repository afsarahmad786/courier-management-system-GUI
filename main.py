import tkinter as tk
from tkinter import *

# window = Tk()

def showsubmit():
    root = Tk()
    root.messagebox.showinfo("Message", "Some message you want the users to see")
    mainloop()
def Login():

    root = Tk()
    root.geometry('420x200')

    root.title("Welcome to Login")


    label_1 = Label(root, text="Username",fg="red")
    label_2 = Label(root, text="Password",fg="red")

    entry_1 = Entry(root)
    entry_2 = Entry(root)

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)



    checkbox = Checkbutton(root, text="Keep me logged in")
    checkbox.grid(columnspan=2)
    MyButton1 = Button(root, text="Submit", width=10,fg="white",bg="blue" ,command=showsubmit)
    MyButton1.grid(row=3, column=0, sticky=E, columnspan=2)
    MyButton1 = Button(root, text="new user", width=10,fg="white",bg="blue")
    MyButton1.grid(rowspan=5)
    mainloop()

def consignment():
    root = Tk()
    root.geometry('420x200')

    root.title("Welcome to Track Consignment")

    label_1 = Label(root, text="Mobile No.",fg="red")
    label_2 = Label(root, text="Consignment No.",fg="red")

    entry_1 = Entry(root)
    entry_2 = Entry(root)

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    MyButton1 = Button(root, text="Submit", width=10,bg="blue",fg="white")
    MyButton1.grid(columnspan=3)

    mainloop()


def Register():
    root = Tk()
    root.geometry('420x200')

    root.title("Welcome to Register")

    label_1 = Label(root, text="Name",fg="red")
    label_2 = Label(root, text="Reg. No",fg="red")
    label_3 = Label(root, text="mobile No",fg="red")
    label_4 = Label(root, text="Email",fg="red")

    entry_1 = Entry(root)
    entry_2 = Entry(root)
    entry_3 = Entry(root)
    entry_4 = Entry(root)

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    label_3.grid(row=2, sticky=E)
    label_4.grid(row=3, sticky=E)
    entry_3.grid(row=2, column=1)
    entry_4.grid(row=3, column=1)
    checkbox = Checkbutton(root, text="male")
    checkbox.grid(columnspan=2)
    checkbox = Checkbutton(root, text="female")
    checkbox.grid(columnspan=2)
    checkbox = Checkbutton(root, text="Keep me logged in")
    checkbox.grid(columnspan=2)
    MyButton1 = Button(root, text="Submit", width=10,command=showsubmit,bg="blue",fg="white")
    MyButton1.grid(columnspan=2)

    mainloop()



root = tk.Tk()
root.title("Welcome to LikeGeeks app")

lbl =Label(root, text="Hello Welcome to Courier Management System", font=("Arial Bold", 30))
lbl.grid(column=5, row=5)
lbl.pack(side=tk.LEFT,padx=20, pady=20)



# root.geometry('420x200')

frame = tk.Frame(root)
frame.pack()
root.title("Welcome to Courier Management System app")
# lbl =Label(root, text="Hello welcome to Courier Management System", font=("Arial Bold", 46))

slogan = tk.Button(frame,
                   text="Login",bg="blue", fg="white",width=10,command=Login)
slogan.pack(side=tk.LEFT)

button1 = tk.Button(frame,
                   text="Registration",
                    bg="blue", fg="white",width=10,command=Register)
button1.pack(side=tk.LEFT,padx=20, pady=20)
button2 = tk.Button(frame,
                   text="Track Consignment",
                    bg="blue", fg="white",command=consignment)
button2.pack(side=tk.LEFT,padx=20, pady=20)

button = tk.Button(frame,
                   text="QUIT",
                   bg="red", fg="white",
                   command=quit,width=10)
button.pack(side=tk.LEFT)
root.mainloop()