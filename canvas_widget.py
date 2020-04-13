from tkinter import *
root=Tk()
def hello():
    print("you have just seen how to use canvas in python"
          " ")

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

#line goes from the point x1,y1 to x2,y2
#can_widget.create_line(0,0,800,400,fill="red")
#can_widget.create_line(0,400,800,0,fill="red")


#to create a rectangle specify parameters in this order- corrds of top left and coords of bottom right
can_widget.create_rectangle(90,50,700,300,fill="grey")
can_widget.create_oval(600,300,200,350,fill="green")

can_widget.create_text(400,200,text="THIS IS HOW YOU USE CANVAS")

b1=Button(root,fg="green",text="PRESS HERE", command= hello)
b1.pack(side=TOP,padx=500)
root.mainloop()