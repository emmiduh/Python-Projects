import random
import time

print("######### Welcome to the Hangman Game! ##########\n")
name = input("Enter your name: ")
print(f"Hello, {name}! Good luck!\n")
time.sleep(2)
print("The game is loading!\n")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["abundance", "energy", "light", "joy", "skill", "time", "overseas", "purpose", "travel"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ''


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input(f"This is the Hangman Word: {display} Enter your guess: \n")
    guess = guess.strip()
    
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print('Invalid input, Try a letter\n')
        hangman()
    
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index +1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')
    
    elif guess in already_guessed:
        print('Try another letter.\n')
    
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print('  _____ \n'
                  ' |     | \n'
                  ' |      \n'
                  ' |      \n'
                  ' |      \n'
                  ' |      \n'
                  ' |      \n'
                  '_|_     \n')
            print(f'Wrong guess. {str(limit - count)} guesses remaining\n')
        
        elif count == 2:
            time.sleep(1)
            print('  _____ \n'
                  ' |     | \n'
                  ' |     |\n'
                  ' |      \n'
                  ' |      \n'
                  ' |      \n'
                  ' |      \n'
                  '_|_     \n')
            print(f'Wrong guess. {str(limit - count)} guesses remaining\n')

        elif count == 3:
            time.sleep(1)
            print('  _____ \n'
                  ' |     | \n'
                  ' |     | \n'
                  ' |     | \n'
                  ' |      \n'
                  ' |      \n'
                  ' |      \n'
                  '_|_     \n')
            print(f'Wrong guess. {str(limit - count)} guesses remaining\n')

        elif count == 4:
            time.sleep(1)
            print('  _____ \n'
                  ' |     | \n'
                  ' |     | \n'
                  ' |     | \n'
                  ' |     o \n'
                  ' |      \n'
                  ' |      \n'
                  '_|_     \n')
            print(f'Wrong guess. {str(limit - count)} guesses remaining\n')

        elif count == 5:
            time.sleep(1)
            print('  _____ \n'
                  ' |     | \n'
                  ' |     | \n'
                  ' |     | \n'
                  ' |     o \n'
                  ' |    /|\\ \n'
                  ' |    / \\ \n'
                  '_|_     \n')
            print(f'Wrong guess. You are hanged!!\n')
            print(f'The word was: {already_guessed}, {word}')
            play_loop()
    
    if word == '_' * length:
        print("Congrats! You have guess the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

def play_loop():
    global play_game
    play_game = input('Do you want to play again? y = yes, n = no \n')
    while play_game not in ["y", 'n', 'Y', 'N']:
        play_game = input('Do you want to play again? y = yes, n = no \n')
    if play_game == "y":
        main()
        hangman()
    elif play_game == 'n':
        print("Thanks for playing, we expect you back again!")
        exit()


main()

hangman()