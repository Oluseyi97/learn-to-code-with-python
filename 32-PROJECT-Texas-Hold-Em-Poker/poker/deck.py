import random

class Deck():
    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def add_cards(self, cards):
        self._cards.extend(cards)

    def remove_cards(self, number):
        cards_to_remove = self._cards[:number]
        del self._cards[0:number]
        return cards_to_remove

    def shuffle(self):
        random.shuffle(self._cards)