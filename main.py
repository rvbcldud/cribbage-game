from Deck import Deck
from Hand import Hand
from Card import Card

'''
CRIBBAGE GAME
'''

deck = Deck()

deck.shuffle()

p1 = Hand()
p2 = Hand()

deck.deal_cards(6, p1)
deck.deal_cards(6, p2)

random_card = deck.random_card() # IT IS CALLED A CUT CARD  

print('Player 1\'s cards: ')
p1.display_hand()

print('\nPlayer 2\'s cards: ')
p2.display_hand()

print('\nRandom card: ')
print(random_card.read_card())

