from enum import Enum
from dataclasses import dataclass

class BoardState(Enum):
    P1_ACTION = 1 # waiting on action from p1
    P2_ACTION = 2 # waiting on action from p2
    P2_RESPONSE_TO_ACTION = 3
    P1_RESPONSE_TO_ACTION = 4
    P2_RESPONSE_TO_COUNTER = 5
    P1_RESPONSE_TO_COUNTER = 6

class Card(Enum):
    RED = 1
    GREEN = 2
    BLACK = 3
    COUNTER = 4
    

@dataclass
class CardZone:
    RED: int
    GREEN: int
    BLACK: int

@dataclass
class Realm:
    Grave: CardZone
    Hand: CardZone
    Tab: CardZone

@dataclass
class FullAction:
    Action: Card
    Target: Card

@dataclass
class Game:
    P1: Realm
    P2: Realm
    Action: FullAction
    State: BoardState

# P1Realm = Realm(CardZone(0,0,0), CardZone(1,2,2), CardZone(1,2,0))
# A1 = FullAction(Card.RED, Card.BLACK)
# print(P1Realm)
# print(A1)


# Examples
# player = PlayerState(name="Alice", health=100, position=(0, 0))
# class Card(Enum)