import unittest
from day7 import Day7


class Day7Test(unittest.TestCase):
    def test_min_fuel_for_alingn_1(self):
        d = Day7('day7_input1.txt')

        self.assertEqual(d.min_fuel_for_alingn(), 37)

    def test_min_fuel_for_alingn_2(self):
        d = Day7('day7_input2.txt')

        self.assertEqual(d.min_fuel_for_alingn(), 355764)

    def test_min_fuel_for_alingn2_1(self):
        d = Day7('day7_input1.txt')

        self.assertEqual(d.min_fuel_for_alingn2(), 168)

    def test_min_fuel_for_alingn2_2(self):
        d = Day7('day7_input2.txt')

        self.assertEqual(d.min_fuel_for_alingn2(), 99634572)

    if __name__ == '__main__':
        unittest.main()