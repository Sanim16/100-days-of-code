from art import logo, vs
from game_data import data
import random

def random_contestant():
    """
    selects a random member of the data set for comparison
    :return: a random member of the data
    """
    return data[random.randint(0, len(data)-1)]

def check_pick(player_choice):
    """
    Checks to confirm if player picked the contestant with more followers
    :param player_choice: the players choice of contestant
    :return: True if player picked right choice else False
    """
    if player_choice == "a" or player_choice == "b":
        if players[f'{player_choice}']['follower_count'] == max(players['a']['follower_count'], players['b']['follower_count']):
            return True

def present_contestants(contestant):
    return f"{players[contestant]['name']}, a {players[contestant]['description']}, from {players[contestant]['country']}."

players = {
    "a": random_contestant(),
}

print(logo)
score = 0
play_game = True
while play_game:
    players['b'] = random_contestant()
    print(f"Compare A: {present_contestants('a')}")
    print(vs)
    print(f"Against B: {present_contestants('b')}")
    pick = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_pick(pick):
        score += 1
        print("\n" * 50)
        print(logo)
        print(f"You're right! Current score: {score}.")
        if score % 3 == 0:
            players['a'] = players['b']
        else:
            players['a'] = players[pick]
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False
