from tkinter import *
root = Tk()
root.geometry("655x333")

def hello():
    print("you are using tkinter button function")


def owner():
    print("want to know the owner of this laptop")

def name():
    print("name of the owner is Saksham Jain")
f1= Frame(root,borderwidth=8,bg="grey", relief= SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1,fg="red",text="print now", command= hello)
b1.pack(side=LEFT,padx=20)
b2=Button(f1,fg="red",text="print now",command=owner)
b2.pack(side=LEFT,padx=20)
b3=Button(f1,fg="red",text="print now",command=name)
b3.pack(side=LEFT,padx=20)


root.mainloop()