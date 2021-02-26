from tkinter import *
from time import *
import datetime

root = Tk()
root.title('KK Saat')

def clock():
    text = strftime('%H:%M:%S')
    label.config(text=text)
    label.after(1000,clock)

def countdown():
    delta = datetime.datetime(2021,1,2,14,0,0) - datetime.datetime.now()
    days = delta.days
    hours, rem = divmod(delta.seconds,3600)
    minutes, seconds = divmod(rem,60)
    text = fillzero(str(hours)) + ':' + fillzero(str(minutes)) + ':' + fillzero(str(seconds))
    label.config(text=text)
    label.after(1000,countdown)

def fillzero(x):
    return x.zfill(2)

label = Label(root, font=('ds-digital',100), background='black', foreground='white')
label.pack(anchor='center')

#clock()
countdown()

mainloop()