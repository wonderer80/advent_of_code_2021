import unittest
from day1 import Day1


class Day1Test(unittest.TestCase):
    def test_count_increments_1(self):
        d = Day1('day1_input1.txt')
        result = d.count_increments()
        self.assertEqual(result, 7)

    def test_count_increments_2(self):
        d = Day1('day1_input2.txt')
        result = d.count_increments()
        self.assertEqual(result, 1475)

    def test_count_incremental_sums_1(self):
        d = Day1('day1_input1.txt')
        result = d.count_incremental_sums(3)
        self.assertEqual(result, 5)

    def test_count_incremental_sums_2(self):
        d = Day1('day1_input2.txt')
        result = d.count_incremental_sums(3)
        self.assertEqual(result, 1516)

if __name__ == '__main__':
    unittest.main()
