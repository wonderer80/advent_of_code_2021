import unittest
from day5 import Day5


class Day5Test(unittest.TestCase):
    def test_get_overlapped_point_count_1(self):
        d = Day5('day5_input1.txt')

        self.assertEqual(d.get_overlapped_point_count(), 5)

    def test_get_overlapped_point_count_2(self):
        d = Day5('day5_input2.txt')

        self.assertEqual(d.get_overlapped_point_count(), 5632)

    def test_get_overlapped_point_count2_1(self):
        d = Day5('day5_input1.txt')

        self.assertEqual(d.get_overlapped_point_count2(), 12)

    def test_get_overlapped_point_count2_2(self):
        d = Day5('day5_input2.txt')

        self.assertEqual(d.get_overlapped_point_count2(), 5632)

    if __name__ == '__main__':
        unittest.main()