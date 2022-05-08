from classes import Deck, Player
import time

# generate deck of 52 cards
while True:
    d1 = Deck()

    # randomize the deck
    d1.shuffle_deck()

    # deal cards, half deck to each player
    mid_index = (len(d1.whole_deck)//2)+1
    p1 = Player('Player 1',d1.whole_deck[:mid_index])
    p2 = Player('Player 2',d1.whole_deck[mid_index:])

    # play cards on table - remove one card from each players deck to compare
    p1_card = p1.play()
    p2_card = p2.play()

    # show cards played on table - print str dunder method from class for each player 
    print(p1)
    print(p2)

    # compare cards on table - use vals dict values to compare p1_card to p2_card
    if p1_card.value < p2_card.value:
        time.sleep(1)
        print(f"Player 2 wins!")
        break
    elif p1_card.value > p2_card.value:
        time.sleep(1)
        print("Player 1 wins!")
        break
    else:
        # if cards are equal, play again until one wins
        print("\nTie! Drawing again for this round..\n")
        time.sleep(2)
        continue
    
    # winner collects all cards on table
    
    # 
