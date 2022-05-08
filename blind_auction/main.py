import replit
from classes import Bidder

bidders = {}
print("Welcome to the Auction!")

bid_on = True

while True:
    while bid_on == True:
        
        name = input("What is your name?: ")
        bid = input("What is your bid?: $")

        bidder = Bidder(name, bid)
        bidders[name] = int(bid)
        other_bidders = input("Are there any other bidders? (y/n): ").lower()

        if other_bidders == 'y' or other_bidders == 'yes':
            replit.clear()
            continue
        elif other_bidders =='n' or other_bidders == 'no':
            replit.clear()
            bid_on = False
            
    # work out who has highest bid
    v_list = list(bidders.values())
    k_list = list(bidders.keys())
    pos = v_list.index(max(v_list))
    winner = k_list[pos]
    bid_list = []
    
    print("Bidders\n --------")

    for k,v in bidders.items():
        print(f"{k}: ${v}")

    print(f"The winner of the auction is {winner} for ${bidders[winner]}")
    break
