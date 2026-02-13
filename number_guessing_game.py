# Number Guessing Game
# Simple Python Project
# Author: Mr. Selfish 😎

import random

def guessing_game():
    number = random.randint(1, 10)
    attempts = 0

    print("🎯 Welcome to Number Guessing Game")
    print("Guess the number between 1 and 10")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low ❌")
        elif guess > number:
            print("Too high ❌")
        else:
            print("🎉 Correct!")
            print("You guessed the number in", attempts, "attempts")
            break

# Start game
guessing_game()
