from tkinter import *
import random

window = Tk()
window.geometry('400x400')
window.title("Rock Paper Scissors Game")
window.resizable(width=False, height=False)
window.config(bg='light blue')

Label(window, text='Rock, Paper, Scissors', font='arial 20 bold', bg='light blue').pack()

user_pick = StringVar()
Label(window, text="Choose any one of rock, paper, scissors: ", font='arial 15 bold', bg='light blue').place(x=20, y=70)
Entry(window, font='arial 15', textvariable=user_pick, bg='antiquewhite2').place(x=90, y=130)

computer_choice = random.randint(1,3)
if computer_choice ==1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

Result = StringVar()

def play_game():
    user_choice = user_pick.get()
    if user_choice == computer_choice:
        Result.set("It's a tie! You both chose the same option")
    elif user_choice == "rock" and computer_choice == "paper":
        Result.set("You lose! Computer chose paper")
    elif user_choice == "rock" and computer_choice == "scissors":
        Result.set("You win! Computer chose scissors")
    elif user_choice == "paper" and computer_choice == "scissors":
        Result.set("You lose! Computer chose scissors")
    elif user_choice == "paper" and computer_choice == "rock":
        Result.set("You win! Computer chose rock")
    elif user_choice == "scissors" and computer_choice == "rock":
        Result.set("You lose! Computer chose rock")
    elif user_choice == "scissors" and computer_choice == "paper":
        Result.set("You win! Computer chose paper")
    else:
        Result.set("Invalid choice: Choose any one of rock, paper, scissors")
    

def Reset():
    Result.set("")
    user_pick.set("")


def Exit():
    window.destroy()

Entry(window, font="arial 10 bold", textvariable=Result, bg='antiquewhite2', width=50).place(x=25, y=250)

Button(window, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play_game).place(x=150, y=190)

Button(window, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(window, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310) 

window.mainloop()