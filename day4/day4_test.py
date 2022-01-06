import unittest
from day4 import Day4


class Day4Test(unittest.TestCase):
    def test_first_bingo_final_score_1(self):
        d = Day4('day4_input1.txt')

        self.assertEqual(d.first_bingo_final_score(), 4512)

    def test_first_bingo_final_score_2(self):
        d = Day4('day4_input2.txt')

        self.assertEqual(d.first_bingo_final_score(), 41503)

    def test_last_bingo_final_score_1(self):
        d = Day4('day4_input1.txt')

        self.assertEqual(d.last_bingo_final_score(), 1924)

    def test_last_bingo_final_score_2(self):
        d = Day4('day4_input2.txt')

        self.assertEqual(d.last_bingo_final_score(), 3178)

    if __name__ == '__main__':
        unittest.main()