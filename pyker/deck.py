import random
from card import Card, Rank, Suit


class Deck:
    def __init__(self):
        self.cards = self._create_deck()

    def _create_deck(self):
        return [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def __str__(self):
        return " ".join(str(card) for card in self.cards)
