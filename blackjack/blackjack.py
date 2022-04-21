import random
from classes import *

'''
    BlackJack. Winner of the hand wins 10 points.
'''

J = 10
Q = 10
K = 10
A = 11

cards = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
random.shuffle(cards)

player_score = 0
dealer_score = 0

'''
    Grabs one random value from cards list.

    returns random value from cards list
'''

def randomize():
    rand_index = random.randint(0, len(cards))
    return cards[rand_index-1]

def ace(dealer_hand):
    if dealer_hand[0] == 10 or dealer_hand[1] == 10:
        return 11
    elif sum(dealer_hand) >= 17:
        return 1

def deal_cards(hand):
    hand.append(randomize())
    hand.append(randomize())
    return hand

'''
    return 0 if bust, return 1 to continue game
'''
def check_bust(hand_sum):
    if hand_sum > 21:
        return True
    else:
        return False

def dealer_turn(dealer_hand):
    dealer_total = sum(dealer_hand)
    if dealer_total > 21:
        print("Dealer busted. You win!")
        return False
    elif dealer_total == 21:
        print("Dealer has 21, dealer wins")
        return True

def hit(hand):
    r = randomize()
    hand.append(r)
    print(f"You get a {r}")
    return hand

def main():
    player_hand = []
    dealer_hand = []
    
    start = input("Press Enter to deal hands")

    if start == "":
        player_cards = deal_cards(player_hand)
        dealer_cards = deal_cards(dealer_hand)
        
    else:
        pass
    print(f"Your cards: {player_cards}")
    print(f"Dealer's cards: {dealer_cards}")
    ace(dealer_hand)

    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)

    if player_total == 21:
        print("Blackjack! Player wins!")
        return True
    elif dealer_total == 21:
        print("Blackjack! Dealer wins!")
        return False

    while player_total < 21 or dealer_total < 21:

        action = input("\n1.) Hit\n2.) Stay\nChoose action: ")
        if action == '1':
            player_total = sum(hit(player_hand))
            print(player_total)
            if player_total > 21:
                print("You busted. You lose")
                break
            if player_total == 21:
                print("You hit 21! You win!")
                global player_score 
                player_score += 10
                break
        if action == '2':
            # when player chooses option 2 to stay, then it becomes dealer's turn
            dealer_win = dealer_turn(dealer_hand)

            if dealer_win == True:
                print("You lose this round")

print("Welcome to a game of Blackjack!")
while True:

    player_win = main()
    if player_win == True:
        continue
    play_again = input("Play another round? (y/n): ").lower()
    if play_again == 'y' or play_again == 'yes':
        continue
    else:
        break
