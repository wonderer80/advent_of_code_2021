import unittest
from day9 import Day9


class Day9Test(unittest.TestCase):
    def test_sum_risk_level_1(self):
        d = Day9('day9_input1.txt')

        self.assertEqual(d.sum_risk_level(), 15)

    def test_sum_risk_level_2(self):
        d = Day9('day9_input2.txt')

        self.assertEqual(d.sum_risk_level(), 500)

    def test_multiply_three_largest_basins_1(self):
        d = Day9('day9_input1.txt')

        self.assertEqual(d.multiply_three_largest_basins(), 1134)

    def test_multiply_three_largest_basins_2(self):
        d = Day9('day9_input2.txt')

        self.assertEqual(d.multiply_three_largest_basins(), 1134)

    if __name__ == '__main__':
        unittest.main()