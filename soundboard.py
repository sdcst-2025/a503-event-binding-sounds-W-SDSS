import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p

window = tk.Tk()
window.title("soundboard")
window.geometry("350x300")
window.attributes("-topmost", True)

def dog():
    p.playsound("dog.mp3")

#
dog = tk.PhotoImage(file="dog.png").subsample(5,5)
cat = tk.PhotoImage(file="cat.png").subsample(5,5)
chicken = tk.PhotoImage(file="chicken.png").subsample(5,5)
hourse = tk.PhotoImage(file="hourse.png").subsample(5,5)
pig = tk.PhotoImage(file="hourse.png").subsample(5,5)
cow = tk.PhotoImage(file="hourse.png").subsample(5,5)

b1=tk.Button(window, text="Dog", image=dog, compound="top", width=100, height=100, command="dog")
b2=tk.Button(window, text="Cat", image=cat, compound="top", width=100, height=100)
b3=tk.Button(window, text="Chicken", image=chicken, compound="top", width=100, height=100)
b4=tk.Button(window, text="Hourse", image=hourse, compound="top", width=100, height=100)
b5=tk.Button(window, text="Pig", image=pig, compound="top", width=100, height=100)
b6=tk.Button(window, text="Cow", image=cow, compound="top", width=100, height=100)

b1.place(x=10, y=10)
b2.place(x=120, y=10)
b3.place(x=230, y=10)
b4.place(x=10, y=120)
b5.place(x=120, y=120)
b6.place(x=230, y=120)
#

window.mainloop()