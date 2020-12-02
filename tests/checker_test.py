from src.sample.env import *
import unittest
from unittest.mock import *


class CheckerTest(unittest.TestCase):
    def test_checker_after_17(self):
        checker = Checker()
        file = 'nastolatki.wav'
        checker.mp3.getTime = Mock(name='getTime')
        checker.mp3.getTime.return_value = 18
        checker.mp3.wavWasPlayed = Mock(name='wavWasPlayed')
        checker.mp3.wavWasPlayed.return_value = True
        res = checker.mp3.wavWasPlayed(file)
        self.assertEqual(res, True)

    def test_checker_before_17(self):
        checker = Checker()
        file = 'nastolatki.wav'
        checker.mp3.getTime = Mock(name='getTime')
        checker.mp3.getTime.return_value = 16
        checker.mp3.resetWav = Mock(name='resetWav')
        checker.mp3.resetWav.return_value = False
        res = checker.remainder(file)
        self.assertEqual(res, False)