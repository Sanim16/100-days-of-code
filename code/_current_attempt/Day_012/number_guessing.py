import art
import random

# TODO-1: Print logo and welcome user.

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# TODO-2: Select a random number between 1 and 100 then store in variable called guess.

guess = random.randint(1,100)
print(f"Pssst, the correct answer is {guess}")

# TODO-3: Ask player to select difficulty level and store in variable called difficulty.

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# TODO-4: create a variable called lives, and set it based on difficulty selected then.

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid choice, try the easy level.")
    lives = 10

# TODO-5: loop - Inform user of available lives and ask user to guess the random number
#  selected, convert user input to int. if correct user has won and if not reduce lives
#  by 1 till no lives left.

game_on = True
while game_on:
    if lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == guess:
            print(f"You got it! The answer was {guess}.")
            game_on = False
        elif player_guess > guess:
            lives -= 1
            print("Too high.")
            print("Guess again.")
        else:
            lives -= 1
            print("Too low.")
            print("Guess again.")
    else:
        game_on = False
        print("You've run out of guesses. you lose.")
