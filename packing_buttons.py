from tkinter import *
root = Tk()
root.geometry("655x333")

def hello():
    print("you are using tkinter button function")

f1= Frame(root,borderwidth=8,bg="grey", relief= SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1,fg="red",text="print now", command= hello)
b1.pack(pady=20)
b2=Button(f1,fg="red",text="print now")
b2.pack(pady=20)
b3=Button(f1,fg="red",text="print now")
b3.pack(pady=20)
b4=Button(f1,fg="red",text="print now")
b4.pack(pady=20)
b5=Button(f1,fg="red",text="print now")
b5.pack(pady=20)


root.mainloop()