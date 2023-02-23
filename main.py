import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
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


def comp_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "C":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c)\n").upper()

        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1

    print(f"Correct! The number was {guess}")


comp_guess(1000)
