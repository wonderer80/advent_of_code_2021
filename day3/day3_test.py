import unittest
from day3 import Day3


class Day3Test(unittest.TestCase):
    def test_get_power_consumption_1(self):
        d = Day3('day3_input1.txt')
        result = d.get_power_consumption()
        self.assertEqual(result, 198)

    def test_get_power_consumption_2(self):
        d = Day3('day3_input2.txt')
        result = d.get_power_consumption()
        self.assertEqual(result, 3309596)

    def test_get_life_support_rating_1(self):
        d = Day3('day3_input1.txt')
        result = d.get_life_support_rating()
        self.assertEqual(result, 230)

    def test_get_life_support_rating_2(self):
        d = Day3('day3_input2.txt')
        result = d.get_life_support_rating()
        self.assertEqual(result, 2981085)

    if __name__ == '__main__':
        unittest.main()