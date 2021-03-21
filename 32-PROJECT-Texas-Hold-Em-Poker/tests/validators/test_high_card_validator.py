import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardsValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades")
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")

        cards = [
            Card(rank = "5", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Queen", suit = "Spades"),
            ace_of_diamonds
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )