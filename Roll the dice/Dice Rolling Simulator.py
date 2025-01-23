import tkinter as tk
from PIL import Image, ImageTk
import random
import os

window = tk.Tk()
window.geometry("400x400")
window.title("Dice Rolling Simulator Game")

BlankLine = tk.Label(window, text="")
BlankLine.pack()

Heading = tk.Label(window, 
                    text="Hello from Dice Rolling Simulator Game", 
                    bg="blue", 
                    fg="white",
                    font='arial 16 bold'
                   )
Heading.pack(pady=20)

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

def roll_dice():
    try:
        selected_dice = random.choice(dice)
        dice_path = os.path.join(os.getcwd(), selected_dice)
        DiceImage = ImageTk.PhotoImage(Image.open(dice_path))
        ImageLabel.config(image=DiceImage)
        ImageLabel.image = DiceImage
    except Exception as e:
        print(f"An error occurred: {e}")
        ErrorLabel.config(text=f"An error occurred: {e}")


DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tk.Label(window, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack(expand=True)

RollButton = tk.Button(window, text="Roll the Dice", command=roll_dice, bg="blue", fg="white", font='arial 16 bold')
RollButton.pack(pady=20)

ErrorLabel = tk.Label(window, text="", fg="red", font='arial 16 bold')
ErrorLabel.pack()

window.mainloop()