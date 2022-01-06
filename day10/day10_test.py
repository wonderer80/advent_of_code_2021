import unittest
from day10 import Day10


class Day10Test(unittest.TestCase):
    def test_total_syntax_error_score_1(self):
        d = Day10('day10_input1.txt')

        self.assertEqual(d.total_syntax_error_score(), 26397)

    def test_total_syntax_error_score_2(self):
        d = Day10('day10_input2.txt')

        self.assertEqual(d.total_syntax_error_score(), 290691)

    def test_middle_score_1(self):
        d = Day10('day10_input1.txt')

        self.assertEqual(d.middle_score(), 288957)

    def test_middle_score_2(self):
        d = Day10('day10_input2.txt')

        self.assertEqual(d.middle_score(), 2768166558)

    if __name__ == '__main__':
        unittest.main()