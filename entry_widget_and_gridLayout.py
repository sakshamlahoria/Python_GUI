from tkinter import *

root=Tk()
root.geometry("655x555")

def getvals():
    print(uservalue.get())
    print(passvalue.get())
user=Label(root,text="username")
password=Label(root,text="password")
user.grid()
password.grid(row=2)


#variables in tkinter
#booleanVar , doubleVar , IntVar , StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=2,column=1)


Button(text="Submit",command=getvals).grid()

root.mainloop()