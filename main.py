import random

#User guess version
def guess(x):
    #Generate a random number for the user to try to guess
    random_number = random.randint(1, x)
    
    guess = 0
    #Loop until user guesses correctly
    while guess != random_number:
        #Take user guess as input and compare to random number, respond accordingly
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess == random_number:
            print("Correct!")
            break
        elif guess < random_number:
            print("Too low!")
            continue
        else:
            print("Too high!")
            continue

#Computer guess version
def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    #Loop until guess is correct
    while feedback != "C":
        if low != high:
            #Generate a random number between min and max possible answer as guess
            guess = random.randint(low, high)
        else:
            guess = low
        #Take feedback from user to inform next guess, continue until correct number is guessed
        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c)\n").upper()

        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1

    print(f"Correct! The number was {guess}")
