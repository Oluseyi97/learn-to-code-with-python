class NoCardsValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "No Cards"

    def is_valid(self):
        return len(self.cards) == 0

    def valid_cards(self):
        return []
        # return self.cards 
        # Also works since self.cards in this case is an empty list.pcar