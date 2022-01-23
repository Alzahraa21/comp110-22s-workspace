"""Demonstrating conditionals."""

SECRET: int = 7

print("I am thinking of a number between 1-10, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
   print("You guessed correctly!!!")
   print("Slay.")
else: 
    print("Sorry, you guessed incorrectly. Sad face :(")
    print("Try again sweaty.")
    if guess > SECRET:
        print("You guessed too high.")
    else:
        print("You guessed too low.")

print("Game over.")