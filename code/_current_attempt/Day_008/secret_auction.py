import art

def winning_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bid in bidding_dictionary:
        if bidding_dictionary[bid] > highest_bid:
            highest_bid = bidding_dictionary[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


print(art.logo)

additional_bids = True
bids = {}
while additional_bids is True:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))

    bids = {name: price}

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if more_bids == "no":
        additional_bids = False
    elif more_bids != "yes":
        print("Error entry")
        additional_bids = False
    else:
        print("\n" * 50)

winning_bid(bids)
