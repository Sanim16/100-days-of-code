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
print("welcome to Rock Paper Scissors")
computer_choice = random.randint(0,2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice not in [0, 1, 2]:
    print(f"{player_choice} is not a valid choice, you lose")
else:
    print(f"{options[player_choice]}")
    print("Computer chose:")
    print(f"{options[computer_choice]}")
    if player_choice == computer_choice:
        print("Draw")
    elif player_choice == 0:
        if computer_choice == 1:
            print("Paper wins against rock, You lose.")
        else:
            print("Rock wins against scissors, You win.")
    elif player_choice == 1:
        if computer_choice == 0:
            print("Paper wins against rock, You Win.")
        else:
            print("Scissors win against paper., You lose.")
    else:
        if computer_choice == 0:
            print("Rock wins against scissors., You lose.")
        else:
            print("Scissors win against paper., You win.")
