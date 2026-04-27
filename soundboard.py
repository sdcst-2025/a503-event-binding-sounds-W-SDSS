import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p

window = tk.Tk()
window.title("soundboard")
window.geometry("500x500")
window.attributes("-topmost", True)

p.playsound("dog.mp3")

dog = PhotoImage(file="dog.png")
dog = PhotoImage(file="")
dog = PhotoImage(file="")
dog = PhotoImage(file="")
dog = PhotoImage(file="")

b1=tk.Button(window, text="dog", image=dog)
b2=tk.Button(window, text="")
b3=tk.Button(window, text="")
b4=tk.Button(window, text="")
b5=tk.Button(window, text="")


b1.place(x=10,y=10, width=100, height=100)

window.mainloop()