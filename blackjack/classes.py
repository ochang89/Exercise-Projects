import random
J = 10
Q = 10
K = 10
A = [11,1]
cards = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
player_hand = []
dealer_hand = []

class Player:
    def __init__(self, hand):
        self.hand = hand

    def deal_cards(self):
        rand_index = random.randint(0, len(cards)+1)
        
