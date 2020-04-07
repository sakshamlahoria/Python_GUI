
from tkinter import *
from PIL import Image, ImageTk


saksham_root = Tk()

saksham_root.geometry('544x566')

#for jpg images

image = Image.open('pic.jpg')
photo = ImageTk.PhotoImage(image)

label = label(text="photo")
label.pack()
saksham_root.mainloop()