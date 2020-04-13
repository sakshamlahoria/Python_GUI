from tkinter import *

def saksham(event):
    print(f"you clicked a button just now at {event.x},{event.y}")
root=Tk()
root.title("Events in tkinter")
root.geometry("644x544")

widget=Button(root,text="press here")
widget.pack()

widget.bind('<Button-1>',saksham)
widget.bind('<Double-1>',quit)
root.mainloop()