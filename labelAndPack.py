from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("label and pack")
#imp label options
# text = adds the text
# bd = background
# fr = foreground
# font = sets the font
#1.font=("comicsans", 19,"bold" )
#2.font=("comicsans 19 bold")
# padx = x padding
# pady = y padding
# relief = border styling = SUNKEN = RAISED ,GROOVE, RIDGE

title_label= Label(text="Abdul Rashid Salim Salman Khan (pronounced \n[səlˈmaːn ˈxaːn]; Hindi: About this soundpronunciation (\nhelp·info); 27 December 1965)[4] is an Indian film actor, \nproducer, occasional singer and television personality. In a film \ncareer spanning over thirty years, Khan has received numerous \nawards, including two National Film Awards as a film producer, \nand two Filmfare Awards for acting.[5] He has a significant \nfollowing in Asia and the Indian diaspora worldwide,[6][better \nsource needed] and is cited in the media as one of the most \ncommercially successful actors of both world and Indian cinema.[\n7][8] According to the Forbes 2018 list of Top-Paid 100 Celebrity \nEntertainers in world, Khan was the highest ranked Indian with \n82nd rank with earnings of $37.7 million.[9][10] He is also known \nas the host of the reality show, Bigg Boss since 2010.[11]" ,bg ="red",  fg="white" ,padx= 23, pady=93, font=("comicsans", 19,"bold" ),borderwidth= 3,relief=SUNKEN)

#important pack option
#anchor=nw
#side= top,bottom,left,right
#fill
#padx
#pady

#title_label.pack(side=BOTTOM, anchor= "sw", fill='x')

title_label.pack(side=LEFT,fill='y',padx=19,pady=34)
root.mainloop()