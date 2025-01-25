from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Mad Libs Generator Game")

Label(window, text="Mad Libs Generator Game \nHave Fun!", font="arial 20 bold").pack()
Label(window, text="Choose a Mad Libs template and fill in the fields below:", font="arial 12 bold").pack(pady=5)

frame = Frame(window)
frame.pack(pady=10)

story_label = Label(window, text="", font="arial 12", wraplength=450, justify="left")
story_label.pack(pady=10)

def create_inputs(inputs):
    for widget in frame.winfo_children():
        widget.destroy()
    global entries
    entries = {}
    for i, field in enumerate(inputs):
        Label(frame, text=f"{field}:", font="arial 12").grid(row=i, column=0, padx=5, pady=5, sticky="w")
        entry = Entry(frame, font="arial 12", width=30)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[field] = entry

def madlib1():
    create_inputs(["name", "animals", "profession", "things", "cloth", "place", "verb", "food"])

    def generate_story():
        name = entries["name"].get()
        animals = entries["animals"].get()
        profession = entries["profession"].get()
        things = entries["things"].get()
        cloth = entries["cloth"].get()
        place = entries["place"].get()
        verb = entries["verb"].get()
        food = entries["food"].get()
        story = f"'Say {food}', the photographer said as the camera flashed! {name} and I had gone to {place} to wanted a picture of us dressed as {animals} pretending to be a {profession}. When we saw the photo, it was exactly what I wanted. We booth looked like {things} wearing {cloth} and {verb} --exactly what I had in mind."
        story_label.config(text=story)
        
        story = (
            f"'Say {food}', the photographer said as the camera flashed! {name} and I had gone to {place} to "
            f"get a picture of us dressed as {animals}s pretending to be a {profession}. When we saw the photo, "
            f"it was exactly what I wanted. We both looked like {things}s wearing {cloth} and {verb} -- exactly "
            f"what I had in mind."
        )
        story_label.config(text=story)

    Button(window, text="Generate Story", font="arial 12", command=generate_story, bg="lightblue").pack(pady=5)

def madlib2():
    create_inputs(["Adjective", "Color", "Thing", "Place", "Person", "Adjective (again)", "Insect", "Food", "Verb"])

    def generate_story():
        adj = entries["Adjective"].get()
        color = entries["Color"].get()
        thing = entries["Thing"].get()
        place = entries["Place"].get()
        person = entries["Person"].get()
        adj1 = entries["Adjective (again)"].get()
        insect = entries["Insect"].get()
        food = entries["Food"].get()
        verb = entries["Verb"].get()

        story = (
            f"Today we picked apples from {person}'s Orchard. I had no idea there were so many different varieties "
            f"of apples in the {place}. I ate {adj} apples straight off the tree that tasted like {color}. Then there "
            f"was a {adj1} apple that looked like a {insect}. When our bags were full, we decided to {verb} on the "
            f"grass and eat our fill. When we were full, we laid back and looked at the {thing} above us. We all felt "
            f"extremely lucky to have this {food}."
        )
        story_label.config(text=story)

    Button(window, text="Generate Story", font="arial 12", command=generate_story, bg="lightblue").pack(pady=5)

# Buttons for choosing templates
Button(window, text="The Photographer", font="arial 15", command=madlib1, bg="ghost white").pack(pady=10)
Button(window, text="Apple and Apple", font="arial 15", command=madlib2, bg="ghost white").pack(pady=10)

# Run the application
window.mainloop()