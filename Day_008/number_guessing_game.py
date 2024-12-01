import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
else:
    lives = 5

def guess_the_number(num, turns):
    while turns > 0:
        print(f"You have {turns} attempt(s) remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {num}")
            return
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        turns -= 1
        if turns != 0:
            print("Guess again.")
    print("You've run of of guesses, you lose.")

guess_the_number(number, lives)
