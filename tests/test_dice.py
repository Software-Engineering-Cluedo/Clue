from src.dice import Dice
import unittest


class MyTestCase(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        for i in range(100000):
            roll1, roll2 = dice.roll()
            roll_total = roll1 + roll2
            self.assertEqual(roll_total <=12 and roll_total >= 2, True)


if __name__ == '__main__':
    unittest.main()