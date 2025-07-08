import art
print(art.logo)
import random
from game_data import data


def random_contender():
    random_index = random.randint(0, len(data) - 1)
    return data[random_index]

def compare_contenders(contender_1, contender_2):
    print(f"Compare A: {contender_1['name']}, a {contender_1['description']}, from {contender_1['country']}")
    print(art.vs)
    print(f"Against B: {contender_2['name']}, a {contender_2['description']}, from {contender_2['country']}")


contender_a = random_contender()

score = 0
game_on = True
while game_on:
    contender_b = random_contender()
    compare_contenders(contender_a, contender_b)
    square_off = {"a": contender_a, "b": contender_b}

    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    count = [square_off["a"]['follower_count'], square_off["b"]['follower_count']]

    if square_off[player_choice]['follower_count'] >= max(count):
        contender_a = contender_b
        score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_on = False
