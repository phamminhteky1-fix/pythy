import random

def guessing_game(hard=False):
    secret = random.randint(0, 100)
    print("🎯 Number Guessing Game!")
    print("I'm thinking of a number between 0 and 100.")
    if hard:
        guess = input("You only get one guess: ").lower()
        if guess in ["give up", "quit", "exit"]:
            print(f"You gave up! The number was {secret}.")
        elif guess.isdigit():
            guess_num = int(guess)
            print(f"Too low by {secret - guess_num}" if guess_num < secret else f"Too high by {guess_num - secret}" if guess_num > secret else "🎉 Correct! You aced it!")
        else:
            print("Invalid input.")
    else:
        tries = 0
        while True:
            guess = input("Your guess: ").lower()
            if guess in ["give up", "quit", "exit"]:
                print(f"You gave up! The number was {secret}.")
                break
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            guess_num = int(guess)
            tries += 1
            if guess_num == secret:
                print(f"🎉 Correct! You guessed it in {tries} tries.")
                break
            print("Too low!" if guess_num < secret else "Too high!")