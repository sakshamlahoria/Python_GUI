import cv2
import os
import glob
from tkinter import *
from PIL import Image, ImageTk


root = Tk()

root.geometry("400x300")
root.title("Album")

img_dir = r"C:\Users\saksham\PycharmProjects\tkinter\png images"
data_path = os.path.join(img_dir)
files = glob.glob('r'+ data_path)
data = []

for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
title_label = Label(text="Hey there good lookin!")



def client_exit(self):
    exit()

#mainloop

title_label.pack()
root.mainloop()
