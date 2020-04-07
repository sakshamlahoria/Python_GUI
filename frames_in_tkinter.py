from tkinter import *
root = Tk()
root.geometry("655x333")
f1= Frame(root,bg="grey",borderwidth=6,relief= SUNKEN)
f1.pack(side=LEFT,fill="y",pady=24)

f2=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")


l=Label(f2,text="Welcome to Sublime text")
l.pack(pady=30)


l=Label(f1,text="Project tkinter - Pycharm")
l.pack(pady=42)
root.mainloop()