import tkinter as tk
from tkinter import *
from tkinter import messagebox

# window = Tk()


def Login():

    root = Tk()
    root.geometry('420x200')

    root.title("Welcome to Login")


    label_1 = Label(root, text="Username",fg="red")
    label_2 = Label(root, text="Registration no",fg="red")

    entry_1 = Entry(root)
    entry_2 = Entry(root)

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)




    def submit():
        name = entry_1.get()
        name2 = entry_2.get()
        with open(name+".txt", "r") as rf:
            with open(name2 + ".txt", "r") as nf:
                name = entry_1.get()
                name2 = entry_2.get()
                line=rf.readline(5)
                line2=nf.readline(10)
                if(name==line) or (name2==line2):
                    messagebox.showinfo("Message", "thanks for login")
                else:
                    messagebox.showinfo("Message", "please register first")

            rf.close()
        root.destroy()
    MyButton1 = Button(root, text="Submit", width=10,fg="white",bg="blue" ,command=submit)
    MyButton1.grid(row=3, column=0, sticky=E, columnspan=2)
    MyButton1 = Button(root, text="new user", width=10,fg="white",bg="blue",command=Register)
    MyButton1.grid(rowspan=5)
    mainloop()

def consignment():
    root = Tk()
    root.geometry('420x200')

    root.title("Welcome to Track Consignment")

    label_1 = Label(root, text="Name.",fg="red")
    label_2 = Label(root, text="Registration No.",fg="red")

    entry_1 = Entry(root)
    entry_2 = Entry(root)

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    def submit():

        name = entry_1.get()
        name2 = entry_2.get()
        with open(name + ".txt", "r") as rf:
            with open(name2 + ".txt", "r") as nf:
                name = entry_1.get()
                name2 = entry_2.get()
                if (name=='' and name2==''):
                    messagebox.showinfo("Message", 'enter values')
                line_new=rf.readline(5)
                line = rf.readlines()

                line2 = nf.readline(10)
                if (name == line_new) or (name2 == line2):
                    messagebox.showinfo("Message", line)
                else:
                    messagebox.showinfo("Message", 'register first')

            rf.close()
        root.destroy()
    MyButton1 = Button(root, text="Track", width=10,fg="white",bg="blue" ,command=submit)
    MyButton1.grid(row=3, column=0, sticky=E, columnspan=2)
    MyButton1 = Button(root, text="new user", width=10,fg="white",bg="blue",command=Register)
    MyButton1.grid(rowspan=5)
    mainloop()




def Register():
    root = Tk()
    root.geometry('420x200')

    root.title("Welcome to Register")

    label_1 = Label(root, text="Name",fg="red")
    label_2 = Label(root, text="Reg. No",fg="red")
    label_3 = Label(root, text="mobile No",fg="red")
    label_4 = Label(root, text="Email",fg="red")
    label_5 = Label(root, text="password", fg="red")
    label_6 = Label(root, text="Gender(M/F)", fg="red")

    entry_1 = Entry(root,)
    entry_2 = Entry(root,)
    entry_3 = Entry(root,)
    entry_4 = Entry(root,)
    entry_5 = Entry(root, )
    entry_6 = Entry(root, )

    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    label_3.grid(row=2, sticky=E)
    label_4.grid(row=3, sticky=E)
    entry_3.grid(row=2, column=1)
    entry_4.grid(row=3, column=1)
    label_4.grid(row=4, sticky=E)
    entry_4.grid(row=4, column=1)
    label_5.grid(row=5, sticky=E)
    entry_5.grid(row=5, column=1)
    label_6.grid(row=6, sticky=E)
    entry_6.grid(row=6, column=1)





    def submit():
        name = entry_1.get()
        name2 = entry_2.get()
        name3 = entry_3.get()
        name4 = entry_4.get()

        name5 = entry_5.get()
        name6 = entry_6.get()

        with open(name+".txt", "w") as wf:
            with open(name2 + ".txt", "w") as wff:
                with open(name3 + ".txt", "w") as wff3:
                    with open(name4 + ".txt", "w") as wff4:
                        with open(name5 + ".txt", "w") as wff5:
                            with open(name6 + ".txt", "w") as wff6:

                                name = entry_1.get()
                                name2 = entry_2.get()
                                name3 = entry_3.get()
                                name4 = entry_4.get()
                                name5 = entry_5.get()
                                name6 = entry_6.get()

                                wf.write(name+'\n')
                                wf.write(name2+'\n')
                                wf.write(name3+'\n')
                                wf.write(name4+'\n')
                                wf.write(name5+'\n')
                                wf.write(name6+'\n')

                        wf.close()
                        wff.close()
                        wff3.close()
                        wff4.close()
                        wff5.close()
                        wff6.close()
                        messagebox.showinfo('info','thanks for register')
        root.destroy()

    MyButton1 = Button(root, text="Submit", width=10,command=submit,bg="blue",fg="white")
    MyButton1.grid(row=9,column=1)




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