import unittest

from PlayingCard import *
from BlackJack import *
from TestInput import TestInput
from ConsoleInput import ConsoleInput


class MyTestCases(unittest.TestCase):
    playingCard = PlayingCard()
    blackJack = BlackJack()
    testInput = TestInput() #ConsoleInput()

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

    # blackjack specific unit tests
    def test_getNumberOfPlayers(self):
        self.testInput.setTestIntegerValues([1,2,3])
        # What is the point in setting up a list if I'm only retrieving one value for the test?
        self.blackJack.set_input(TestInput())
        self.assertEqual(3,self.blackJack.get_number_of_players())

    def test_scoreHand(self):
        self.testInput.setTestStringValues(["HA","CQ"])
        #alternative way to read from console for test input values to be used
        #hand = []
        #hand.append(self.testInput.getInputString("Add a card to test hand: "))
        #hand.append(self.testInput.getInputString("Add another card to test hand: "))
        self.assertEqual(21,self.blackJack.score_hand(self.testInput.testStringValues))

    def test_validDealInput(self):
       self.testInput.setTestStringValues(["B","S","d"])
       #What is the point in setting up a list if I'm only retrieving one value for the test?
       self.blackJack.set_input(TestInput())
       #Is valid_deal_input() running using the test values here?
       self.assertEqual("D",self.blackJack.valid_deal_input())




if __name__ == '__main__':
    unittest.main()
