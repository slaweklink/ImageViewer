# program to open pictures and resizing them to a fixed size.

from tkinter import *
from PIL import ImageTk, Image
import os
import glob

lista = glob.glob("C:\\Users\Slawek1\PycharmProjects\PhotoSlider\*.jpg") #lists all jpg files in a given directory
number = 0 #for counting the elements in a list

def next_file():
    global number
    global panel
    number_of_files = len(lista)
    print(number_of_files)
    if number == number_of_files-1:
        print("It's the last picture")
    else:
        number += 1
    print(number)
    image2 = ImageTk.PhotoImage(Image.open(lista[number]))
    panel.configure(image = image2)
    panel.image = image2

def previous_file():
    global number
    global panel
    number_of_files = len(lista)
    print(number_of_files)
    if number == 0:
        print("It's the first picture")
    else:
        number -= 1
    print(number)
    image2 = ImageTk.PhotoImage(Image.open(lista[number]))
    panel.configure(image = image2)
    panel.image = image2

okno= Tk()
okno.resizable(0,0)
okno.title("Photo slider")
guzik = Button(text = "Previous", command = previous_file)
guzik.pack(side = TOP)
guzik1 = Button(text = "Next", command = next_file)
guzik1.pack(side = TOP)
guzik2 = Button(text = "Open file")
guzik2.pack(side = TOP)

img = ImageTk.PhotoImage(Image.open(lista[number]))
panel = Label(okno, image = img)
panel.pack(fill = X)


okno.mainloop()
