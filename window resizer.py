from tkinter import *
root=Tk()
root.geometry("544x355")
def update():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")


root.title("updating GUI according to user")
Label(text="window resizer",font="comicsans 19 bold").grid(column=2)

Label(text="width",font="comicsans 19 bold").grid(row=1,column=1)
Label(text="height",font="comicsans 19 bold").grid(row=2,column=1)


width=StringVar()
height=StringVar()

width_entry=Entry(root,textvariable=width).grid(row=1,column=2)
width_height=Entry(root,textvariable=height).grid(row=2,column=2)

Button(text="update",command=update).grid(column=2)
root.mainloop()
