import unittest

from PlayingCard import *
from BlackJack import *
from TestInput import TestInput


class MyTestCases(unittest.TestCase):
    playingCard = PlayingCard()
    blackJack = BlackJack()
    testInput = TestInput()

    #PlayingCard unit tests
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

    def test_dealCards(self):
        deck = self.playingCard.generate_deck()
        no_of_cards = 2
        no_of_hands = 2
        hands = self.playingCard.deal_cards(deck,no_of_cards,no_of_hands)
        self.assertEqual(2,len(hands))
        self.assertEqual(2,len(hands[0]))

    def test_playACardWhenCardInHand(self):
        hand = ["HA","C03"]
        card = "HA"
        self.playingCard.play_a_card(hand,card)
        self.assertEqual(["C03"],hand)

    def test_playACardWhenCardNotInHand(self):
        hand = ["HA", "C03"]
        card = "HQ"
        self.playingCard.play_a_card(hand,card)
        self.assertEqual(["HA","C03"], hand)

    def test_isPlayingACardWhenCardInHand(self):
        hand = ["HA", "C03"]
        card = "HA"
        self.assertTrue(self.playingCard.is_playing_a_card(hand,card))

    def test_isPlayingACardWhenCardNotInHand(self):
        hand = ["HA", "C03"]
        card = "HQ"
        self.assertFalse(self.playingCard.is_playing_a_card(hand,card))

    def test_convertFaceToNumber(self):
        card = "HA"
        self.assertEqual("H01", self.playingCard.convert_face_to_number(card))

    def test_convertFacesToNumbers(self):
        hand = ["HA", "CQ"]
        self.playingCard.convert_faces_to_numbers(hand)
        self.assertEqual(["H01","C12"],hand)

    def test_convertNumberToFace(self):
        card = "H13"
        self.assertEqual("HK", self.playingCard.convert_number_to_face(card))

    def test_convertNumbersToFaces(self):
        hand = ["S11", "C12"]
        self.playingCard.convert_numbers_to_faces(hand)
        self.assertEqual(["SJ","CQ"],hand)

    def test_sortHand(self):
        originalHand = ["SQ","SJ"]
        hand = ["SQ","SJ"]
        self.playingCard.sort_hand(hand)
        self.assertNotEqual(originalHand,hand)

    def test_sortHands(self):
        originalHands = [["SQ","SJ"],["HA", "CQ"]]
        hands = [["SQ","SJ"],["HA", "CQ"]]
        self.playingCard.sort_hands(hands)
        self.assertNotEqual(originalHands,hands)

    def test_scoreHand(self):
        self.testInput.setTestStringValues(["HA","CQ"])
        hand = []
        hand.append(self.testInput.getInputString("blah"))
        hand.append(self.testInput.getInputString("blah"))
        self.assertEqual(21,self.blackJack.score_hand(hand))

    #blackjack specific unit tests
    #def test_validDealInput(self):


if __name__ == '__main__':
    unittest.main()
