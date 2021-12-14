import unittest

from PlayingCard import *
from BlackJack import *
from TestInput import TestInput
from TestOutput import TestOutput


class MyTestCases(unittest.TestCase):
    playingCard = PlayingCard()
    blackJack = BlackJack()
    testInput = TestInput()
    testOutput = TestOutput()

    def setUp(self):
        self.blackJack.set_input(self.testInput)
        self.blackJack.set_output(self.testOutput)

    # blackjack specific unit tests
    def test_getNumberOfPlayers(self):
        self.testInput.setTestIntegerValues([3])
        self.assertEqual(3,self.blackJack.get_number_of_players())

    def test_scoreHand(self):
        hand = ["HA","CQ"]
        self.assertEqual(21,self.blackJack.score_hand(hand))

    '''note: this test passes in isolation but not when running alongside other tests because the test input data gets
    the S appended on the next test.'''
    def test_validDealInput(self):
       self.testInput.setTestStringValues(["d"])
       self.assertEqual("D",self.blackJack.valid_deal_input())

    def test_dealToUserStick(self):
        self.testInput.setTestStringValues(["S"])
        deck = self.playingCard.generate_deck()
        hand = ["HK","CQ"]
        self.blackJack.deal_to_user(deck,hand)
        self.assertEqual(hand,self.testOutput.testOutputValues[1])

    def test_dealToUserDraw(self):
        self.testInput.setTestStringValues(["D","D"])
        deck = self.playingCard.generate_deck()
        hand = ["HK","CQ"]
        self.blackJack.deal_to_user(deck,hand)
        self.assertEqual("Sorry you have gone over the score and are bust",self.testOutput.testOutputValues[2])


if __name__ == '__main__':
    unittest.main()
