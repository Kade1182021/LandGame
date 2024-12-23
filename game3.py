from game2 import *
from collections import Counter
import random

def Draw(r: Realm) -> Realm:
    cards = [Card.RED, Card.GREEN, Card.BLACK]

    # Initialize deck with 10 of each card
    # Subtract the number of cards in the graveyard, hand, and tableau
    
    deck = Counter()
    for card in cards:
        deck[card] = 10 - (getattr(r.Grave, card.name) + getattr(r.Hand, card.name) + getattr(r.Tab, card.name))

    items = list(deck.keys())
    weights = list(deck.values())

    # Pick a random item based on the weights
    drawn_card = random.choices(items, weights=weights, k=1)[0]

    # Increase the drawn card count in Hand
    r.Hand.__dict__[drawn_card.name] += 1

    return r

def TakeAction(game: Game, action: FullAction) -> Game:
    
    return Game

# P1Realm = Realm(CardZone(0,0,0), CardZone(1,2,2), CardZone(1,2,0))
# A1 = FullAction(Card.RED, Card.BLACK)

# print(P1Realm)
# Draw(P1Realm)
# print(P1Realm)