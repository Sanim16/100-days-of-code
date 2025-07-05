import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(card_list):
    card_list.append(random.choice(cards))
    return card_list

def show_cards(player_card_list, computer_card_list):
    print(f"Your cards: {player_card_list}, current score: {sum(player_card_list)}")
    print(f"Computer's first card: {computer_card_list[0]}")

def tally_cards(player_sum, computer_sum):
    if player_sum > 21:
        print("You went over. You lose 😭")
    elif computer_sum > 21:
        print("Opponent went over. You Win 😁")
    elif player_sum > computer_sum:
        print("You win 😁")
    elif player_sum < computer_sum:
        print("You lose 😭")
    elif player_sum == computer_sum:
        print("It's a Draw")

play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
while play_game == "y":
    if play_game == "y":
        print("\n" * 20)
        print(art.logo)
        players_cards = [random.choice(cards), random.choice(cards)]
        computers_cards = [random.choice(cards), random.choice(cards)]
        show_cards(players_cards, computers_cards)

        if sum(players_cards) == 21:
            print("Win with a Blackjack, 😎")
            play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
        elif sum(computers_cards) == 21:
            print("Opponent has Blackjack, You lose 😱")
            play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
        else:
            keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            while keep_dealing == "y":
                deal_cards(players_cards)
                show_cards(players_cards, computers_cards)
                if sum(players_cards) > 21 and players_cards[-1] == 11:
                    players_cards[-1] = 1
                if sum(players_cards) > 21:
                    keep_dealing = "n"
                else:
                    keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            while sum(computers_cards) < 17:
                deal_cards(computers_cards)

            print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
            print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
            tally_cards(sum(players_cards), sum(computers_cards))

            play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

    else:
        print("Bye")
