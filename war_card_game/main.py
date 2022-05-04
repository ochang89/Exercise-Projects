from classes import Deck

# generate deck with 52 cards
d1 = Deck()

# randomize the deck
d1.shuffle_deck()

for i in d1.whole_deck:
    print(i)

