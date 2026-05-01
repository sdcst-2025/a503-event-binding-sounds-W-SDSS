import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p

window = tk.Tk()
window.title("soundboard")
window.geometry("500x500")
window.attributes("-topmost", True)

p.playsound("dog.mp3")

dog = tk.PhotoImage(file="dog.png").subsample(20,20)
cat = tk.PhotoImage(file="cat.png").subsample(20,20)
chicken = tk.PhotoImage(file="chicken.png").subsample(20,20)
hourse = tk.PhotoImage(file="hourse.png").subsample(20,20)

b1=tk.Button(window, text="Dog", image=dog, compound="top")
b2=tk.Button(window, text="Cat", image=cat, compound="top")
b3=tk.Button(window, text="Chicken", image=chicken, compound="top")
b4=tk.Button(window, text="Hourse", image=hourse, compound="top")


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)

window.mainloop()