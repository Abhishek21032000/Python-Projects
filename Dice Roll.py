from tkinter import *
import random

root = Tk()
root.geometry("700x450")
root.title("Roll Dice")

label = Label(root, text="", font=("Times", 260))
label.pack()

def roll():
    dice_faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice_faces)}{random.choice(dice_faces)}')

button = Button(root, text="Let's roll...", width=40, height=5, font=("Times", 10), bg="white", bd=2, command=roll)
button.pack(padx=10, pady=10)

root.mainloop()
