import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def display_cards(player_card_hand, dealer_card_hand):
    print(f"Your cards: {player_card_hand}, current score: {sum(player_card_hand)}")
    print(f"Computer's first card: {dealer_card_hand}")

def final_cards(player_card_hand, dealer_card_hand):
    print(f"Your final hand: {player_card_hand}, final score: {tally_cards(player_card_hand)}")
    print(f"Computer's final hand: {dealer_card_hand}, final score: {tally_cards(dealer_card_hand)}")

def tally_cards(card_hand):
    return sum(card_hand)

def deal_dealer(dealer_card_hand):
    while tally_cards(dealer_card_hand) < 17:
        dealer_card_hand.append(random.choice(cards))
        if dealer_card_hand[-1] == 11 and tally_cards(dealer_card_hand) > 21:
            dealer_card_hand[-1] = 1
    return dealer_card_hand

def compare(player_card_hand, dealer_card_hand):
    """
    compares the players cards and the dealers cards to get a winner
    :param player_card_hand: array containing players cards
    :param dealer_card_hand: array containing dealers cards
    :return:
    """
    if tally_cards(player_card_hand) > 21:
        final_cards(player_card_hand, dealer_card_hand)
        print("You went over. You lose 😭")
    elif tally_cards(dealer_card_hand) > 21:
        final_cards(player_card_hand, dealer_card_hand)
        print("Opponent went over. You win 😁")
    elif tally_cards(player_card_hand) == tally_cards(dealer_card_hand):
        final_cards(player_card_hand, dealer_card_hand)
        print("Draw 🙃")
    elif tally_cards(player_card_hand) > tally_cards(dealer_card_hand):
        final_cards(player_card_hand, dealer_card_hand)
        print("You win 😃")
    else:
        final_cards(player_card_hand, dealer_card_hand)
        print("You lose 😤")

play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_blackjack == "y":
    print("\n" * 50)
    print(logo)
    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]
    display_cards(player_cards, dealer_cards[0])
    if sum(player_cards) > 21:
        player_cards[-1] = 1
    if sum(dealer_cards) > 21:
        dealer_cards[-1] = 1
    if sum(dealer_cards) == 21:
        print(f"Your final hand: {player_cards}, final score: {tally_cards(player_cards)}")
        print(f"Computer's final hand: {dealer_cards}, final score: 0")
        print("Lose, opponent has Blackjack 😱")
    elif sum(player_cards) == 21:
        print(f"Your final hand: {player_cards}, final score: 0")
        print(f"Computer's final hand: {dealer_cards}, final score: {tally_cards(dealer_cards)}")
        print("Win with a Blackjack 😎")
    else:
        deal_cards = "y"
        while deal_cards == "y":
            deal_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal_cards == "y":
                player_cards.append(random.choice(cards))
                display_cards(player_cards, dealer_cards[0])
                if tally_cards(player_cards) == 21:
                    deal_cards = "n"
                elif player_cards[-1] == 11 and tally_cards(player_cards) > 21:
                    player_cards[-1] = 1
                elif tally_cards(player_cards) > 21:
                    deal_cards = "n"

            elif deal_cards == "n":
                tally_cards(player_cards)

        dealer_cards = deal_dealer(dealer_cards)
        compare(player_cards, dealer_cards)
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
print("Goodbye and see you later")
