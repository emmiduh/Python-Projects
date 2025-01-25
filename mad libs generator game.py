from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Mad Libs Generator Game")

Label(window, text="Mad Libs Generator Game \nHave Fun!", font="arial 20 bold").pack()
Label(window, text="Click any one:", font="arial 20 bold").pack()

def madlib1():
    name = input("Enter a name of a person: ")
    animals = input("Enter an animal: ")
    profession = input("Enter a profession: ")
    things = input("Enter a thing: ")
    cloth = input("Enter a cloth: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food: ")
    print(f"'Say {food}', the photographer said as the camera flashed! {name} and I had gone to {place} to wanted a picture of us dressed as {animals} pretending to be a {profession}. When we saw the photo, it was exactly what I wanted. We booth looked like {things} wearing {cloth} and {verb} --exactly what I had in mind.")

def madlib2():
    adj = input("Enter an adjective: ")
    color = input("Enter a color: ")
    thing = input("Enter a thing: ")
    place = input("Enter a place: ")
    person = input("Enter a person: ")
    adj1 = input("Enter an adjective: ")
    insect = input("Enter an insect: ")
    food = input("Enter a food: ")
    verb = input("Enter a verb: ")
    print(f"Today we picked apple from {person}'s Orchard. I had no idea there were so many different varieties of apples in the {place}. I ate {adj} apples straight off the tree that tested like {color}. Then there was a {adj1} apple that looked like a {insect}. When our bag were full, we decided to {verb} on the grass and eat our fill. When we were full, we laid back and looked at the {thing} above us. We all felt extremely lucky to have this {food}.")

Button(window, text="The Photographer", font="arial 15", command=madlib1, bg="ghost white").place(x=60, y=120)
Button(window, text="Apple and Apple", font="arial 15", command=madlib2, bg="ghost white").place(x=60, y=180)

window.mainloop()