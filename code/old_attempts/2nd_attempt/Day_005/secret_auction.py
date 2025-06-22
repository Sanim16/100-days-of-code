from art import logo
print(logo)

def highest_bidder(bidding_dictionary):
    maximum_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > maximum_bid:
            winner = bidder
            maximum_bid = bidding_dictionary[bidder]
    print(f"The winner is {winner} with a bid of ${maximum_bid}")


participants = {}

accept_bid = True
while accept_bid:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))

    participants[name] = bid

    print("Are there any other bidders? Type 'yes or 'no'.")
    new_bidders = input("Only 'yes' will be accepted.\n").lower()
    if new_bidders != "yes":
        accept_bid = False
        highest_bidder(participants)
    else:
        print("\n" * 100)
