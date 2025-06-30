import art

print(art.logo)

additional_bids = True
highest_bid = 0
winner = ""
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

    for bidder in bids:
        if bids[bidder] > highest_bid:
            winner = bidder
            highest_bid = bids[bidder]
print(f"The winner is {winner} with a bid of ${highest_bid}")
