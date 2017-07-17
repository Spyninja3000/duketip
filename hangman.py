from __future__ import print_function
import numpy

name = raw_input("What is your name? ")
#asks for your name

if name.isalpha(): #checks if name is actually made of only letters
    print("Hello, " + name)
else:
    print("That's not a name!")

play = raw_input("Would you like to play Hangman? ")
#makes sure the player wants to play

if play == "Yes": #Lets them play if 'Yes' or a similar input is given
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
    print("Fine. Be like that.")
    exit() #exits because player doesn't want to play
else:
    print("What? Just go on and play.") #gives an option for answers not defined



def hangman_pic(lives): #sets the number of lives before you die and communicates this to the player
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
    elif lives == 0: #exits the player after they die
        print("You're dead as a doornail")
        print("The word was: " + word)
        exit()

# word : The correct word to be guessed
# correctLetters : List of correctly guessed letters

def printBlanks(word, correctLetters): #prints either a space or a guessed letter
    solved = True #assume that player has won until this is disproved
    for l in word:
        l = l.lower() #ensures that the l is lowercase
        if l in correctLetters:
            print(l + " ", end='')
        else:
            print("_ ", end='')
            solved = False #disproves the fact that the player has won
    print('')
    return solved

word_list = ['pencil', 'guess', 'tejas', 'pneumonoultramicroscopicsilicovolcanoconiosis'] #the word(s) that are the answers

correctLetters = [] #empty space for guessed letters to be stored

lives = 6 #start off with 6 lives

word = numpy.random.choice(word_list)

guesses = 0
letters_used = [] #empty variable used to store all used letters

while True: #start of the mega-loop
    print()
    print()
    solved = printBlanks(word, correctLetters) #sets solved as the player's correct guesses

    if solved == True: #tells the player they win if they won
        print('You win!')
        break

    guess = raw_input("Guess a letter ") #asks for a letter

    if (guess in word) and (guess not in letters_used): #correct answer
        print ("Your guess was correct") #tells player they're correct
        letters_used.append(guess) #adds letter guessed to an empty variable
        correctLetters.append(guess) #adds letter guessed to correctLetters
        hangman_pic(lives)
        print("Letter used: " + guess) #prints letter used
    elif (guess not in word) and (guess not in letters_used): #incorrect answer
        guesses += 1
        print("You were wrong") #tells player they were wrong
        letters_used.append(guess) #adds letter guessed to an empty variable
        lives -= 1 #takes away a life for the incorrect answer
        hangman_pic(lives)
        print("Letter used: " + guess)
    elif guess in letters_used: #makes sure there's no penalty for repeated answers
        print("You've already guessed this letter!")
    else:
        print("Wrong")#gives the player a penalty if they somehow broke my system
        lives-=1
