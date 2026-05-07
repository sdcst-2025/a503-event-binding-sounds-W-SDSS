import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p

window = tk.Tk()
window.title("SoundBoard")
window.geometry("350x280")
window.attributes("-topmost", True)

def Dog():
    p.playsound("dog.mp3",block=False)
def Cat():
    p.playsound("cat.mp3",block=False)
def Chicken():
    p.playsound("chicken.mp3",block=False)
def Horse():
    p.playsound("horse.mp3",block=False)
def Pig():
    p.playsound("pig.mp3",block=False)
def Cow():
    p.playsound("cow.mp3",block=False)



dog = tk.PhotoImage(file="dog.png").subsample(5,5)
cat = tk.PhotoImage(file="cat.png").subsample(5,5)
chicken = tk.PhotoImage(file="chicken.png").subsample(5,5)
horse = tk.PhotoImage(file="horse.png").subsample(5,5)
pig = tk.PhotoImage(file="pig.png").subsample(5,5)
cow = tk.PhotoImage(file="cow.png").subsample(5,5)

l1=tk.Label(window, text="Click the button to hear animal sounds!", font=5)
b1=tk.Button(window, text="Dog", image=dog, compound="top", width=100, height=100, command=Dog)
b2=tk.Button(window, text="Cat", image=cat, compound="top", width=100, height=100,  command=Cat)
b3=tk.Button(window, text="Chicken", image=chicken, compound="top", width=100, height=100,  command=Chicken)
b4=tk.Button(window, text="Horse", image=horse, compound="top", width=100, height=100,  command=Horse)
b5=tk.Button(window, text="Pig", image=pig, compound="top", width=100, height=100,  command=Pig)
b6=tk.Button(window, text="Cow", image=cow, compound="top", width=100, height=100,  command=Cow)

l1.place(x=40, y=10)
b1.place(x=10, y=40)
b2.place(x=120, y=40)
b3.place(x=230, y=40)
b4.place(x=10, y=150)
b5.place(x=120, y=150)
b6.place(x=230, y=150)

window.mainloop()