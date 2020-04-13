from tkinter import *
root = Tk()
def getvals():
    print("submitting form ")

    print(f"{namevalue.get(),phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get() ,foodservicevalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get() ,foodservicevalue.get()}\n")

root.geometry("644x344")

#heading
Label(root,text="welcome to saksham world",font="comicsans 13 bold",pady=20).grid(row=0,column=0)

#text values for form
name=Label(root,text="Name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergency=Label(root,text="emergency number")
payment=Label(root,text="payment mode")


#text pack
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)


#tkinnter values for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()
foodservicevalue=IntVar()

#entries for a form

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentvalue)


#packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#checkbox and packing it
foodservice=Checkbutton(text="want to prebook your meals",variable=foodservicevalue)
foodservice.grid(row=6,column=3,pady=15)

#button and packing it and assigning a command
Button(text="submit",command=getvals).grid(row=7,column=3)
root.mainloop()
