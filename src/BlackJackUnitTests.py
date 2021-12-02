import unittest

from PlayingCard import *
from BlackJack import *


class MyTestCases(unittest.TestCase):
    playingCard = PlayingCard()

    def test_standardDeckLengthIs52(self):
        deck = self.playingCard.generate_deck()
        self.assertEqual(52,len(deck))

    # def test_trentineDeckLengthIs40(self):
    #    self.playingCard.trentine_small()
    #    deck = self.playingCard.generate_deck()
    #    self.assertEqual(40, len(deck))
    def test_shuffleCards(self):
        self.assertNotEqual(self.playingCard.generate_deck(),self.playingCard.shuffle_cards(self.playingCard.generate_deck()))

    def test_dealACard(self):
        deck = self.playingCard.generate_deck()
        card = self.playingCard.deal_a_card(deck)
        self.assertEqual(2, len(card))

    def test_convertFaceToNumber(self):
        card = "HA"
        self.assertEqual("H01", self.playingCard.convert_face_to_number(card))

    def test_convertNumberToFace(self):
        card = "H13"
        self.assertEqual("HK", self.playingCard.convert_number_to_face(card))



if __name__ == '__main__':
    unittest.main()
