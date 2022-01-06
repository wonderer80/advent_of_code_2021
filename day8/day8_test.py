import unittest
from day8 import Day8


class Day8Test(unittest.TestCase):
    def test_count_unique_segments_1(self):
        d = Day8('day8_input1.txt')

        self.assertEqual(d.count_unique_segments(), 26)

    def test_count_unique_segments_2(self):
        d = Day8('day8_input2.txt')

        self.assertEqual(d.count_unique_segments(), 26)

    def test_sum_outputs_1(self):
        d = Day8('day8_input0.txt')

        self.assertEqual(d.sum_outputs(), 5353)

    def test_sum_outputs_2(self):
        d = Day8('day8_input1.txt')

        self.assertEqual(d.sum_outputs(), 61229)

    def test_sum_outputs_3(self):
        d = Day8('day8_input2.txt')

        self.assertEqual(d.sum_outputs(), 1070188)

    if __name__ == '__main__':
        unittest.main()