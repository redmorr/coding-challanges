from dataclasses import dataclass
from enum import Enum

"""
Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.
"""


class Suite(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


@dataclass(frozen=True)
class Card:
    face: int  # A 2 ... 10 J Q K
    suite: Suite


class Deck:
    cards: [Card]

    def __init__(self, cards: [Card]):
        self.cards = cards

    def shuffle(self):
        pass

    def deal_hand(self, number: int):
        pass
