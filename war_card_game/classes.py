from card_data import *
import random

'''
    Card class will instantiate a card using elements from nums, suits.
    self.value holds hidden values from vals dictionary, called by the
    num key (values[num] accesses num key's value in vals dictionary).
'''

class Card:
    def __init__(self, num, suit):
        self.suit = suit
        self.num = num
        self.value = vals[num]

    def __str__(self):
        return f"{self.num} of {self.suit}"

'''
    Deck class will iterate through nums and suits tuples in card_data, to
    instantiate a card from Card class.
    After generating all 52 cards, main.py calls shuffle_deck() to shuffle the 
    deck before playing.
'''
class Deck:
    def __init__(self):
        self.whole_deck = []

        for s in suits:
            for n in nums:
                self.whole_deck.append(Card(n,s))

    def shuffle_deck(self):
        random.shuffle(self.whole_deck)
        