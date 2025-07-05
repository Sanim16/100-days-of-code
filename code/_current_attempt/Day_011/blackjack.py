import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(card_list):
    return random.choice(card_list)

play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
while play_game == "y":
    if play_game == "y":
        print("\n" * 20)
        print(art.logo)

        players_cards = [deal_cards(cards), deal_cards(cards)]
        computers_cards= [deal_cards(cards), deal_cards(cards)]

        print(f"Your cards: {players_cards}, current score: {sum(players_cards)}")
        print(f"Computer's first card: {computers_cards[0]}")

        if sum(players_cards) == 21:
            print("blackjack")
        elif sum(computers_cards) == 21:
            print("Black Jack computer wins")
        else:
            keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            while keep_dealing == "y":
                players_cards.append(deal_cards(cards))
                print(f"Your cards: {players_cards}, current score: {sum(players_cards)}")
                print(f"Computer's first card: {computers_cards[0]}")
                if sum(players_cards) > 21:
                    print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
                    print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
                    print("You went over. You lose 😭")
                    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
                    keep_dealing = "n"
                else:
                    keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            while sum(computers_cards) < 17:
                computers_cards.append(deal_cards(cards))

            if sum(players_cards) > 21:
                print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
                print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
                print("You went over. You lose 😭")
            elif sum(computers_cards) > 21:
                print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
                print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
                print("Opponent went over. You Win 😁")
            elif sum(players_cards) > sum(computers_cards):
                print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
                print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
                print("You win 😁")
            elif sum(players_cards) < sum(computers_cards):
                print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
                print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
                print("You lose 😭")
            elif sum(players_cards) == sum(computers_cards):
                print(f"Your final hand: {players_cards}, final score: {sum(players_cards)}")
                print(f"Computer's final hand: {computers_cards}, computer's final score: {sum(computers_cards)}")
                print("It's a Draw")
            play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

    else:
        print("Bye")
