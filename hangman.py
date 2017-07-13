name = raw_input("What is your name? ")

if name.isalpha():
    print("Hello, " + name)
else:
    print "That's not a name!"

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

lives = 3

x = 1
while True:
    print "You are incorrect" % (x)
    x += 1

guess = ""
while guess == "":
    guess = raw_input("You have " + str(lives) + " lives. Guess a letter.")
print(guess)
exit(0)
