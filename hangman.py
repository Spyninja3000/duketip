from __future__ import print_function
import numpy

name = raw_input("What is your name? ")

if name.isalpha():
    print("Hello, " + name)
else:
    print("That's not a name!")

play = raw_input("Would you like to play Hangman? ")

if play == "Yes":
    print("Okay, let's go!")
elif play == "Sure":
    print("Okay, let's go!")
elif play == "Let's Go":
    print("Okay, let's go!")
elif play == "Why Not":
    print("Okay, let's go!")
elif play == "Why Not?":
    print("Okay, let's go!")
elif play == "yes":
    print("Okay, let's go!")
elif play == "No":
    print("Fine. Be like that. You're playing anyways.")
else:
    print("IM TRIGGERED. Just go on and play.")



def hangman_pic(lives):
    if lives == 6:
        print("The noose is tightly set around your neck")
    if lives == 5:
        print("You have 5 lives now")
    if lives == 4:
        print("You have 4 lives now")
    if lives == 3:
        print("You have 3 lives now")
    if lives == 2:
        print("You have 2 lives now. Rope's getting thin...")
    if lives == 1:
        print("You have freaking 1 live left! You're about to die!")
    elif lives == 0:
        print("You're dead as a doornail")
        exit()

# word : The correct word to be guessed
# correctLetters : List of correctly guessed letters

def printBlanks(word, correctLetters):
    solved = True
    for l in word:
        l = l.lower()
        if l in correctLetters:
            print(l + " ", end='')
        else:
            print("_ ", end='')
            solved = False
    print('')
    return solved

word_list = ['pencil']

correctLetters = []

lives = 6

word = 'pencil'

while True:
    hangman_pic(lives)
    solved = printBlanks(word, correctLetters)

    if solved == True:
        print('You win!')
        break

    guesses = 0
    letters_used = ""

    guess = raw_input("Guess a letter ")

    if guess in word and guess not in letters_used:
        print ("Your guess was correct")
        letters_used += guess
        correctLetters.append(guess)
        print("Letter used: " + letters_used)
    elif guess not in word and guess not in letters_used:
        guesses += 1
        print("You were wrong")
        letters_used += guess
        lives -= 1
        hangman_pic(lives)
        print("Letter used: " + letters_used)
    else:
        print("Wrong")
        lives-=1

