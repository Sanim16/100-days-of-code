import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
computer_choice = random.randint(0,2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[player_choice])
print("Computer chose:")
print(options[computer_choice])
if player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You win!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You win!")
    else:
        print("You lose")
elif player_choice == 2:
    if computer_choice == 0:
        print("You lose")
    else:
        print("You win!")
else:
    print("Invalid choice, you lose")
