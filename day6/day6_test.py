import unittest
from day6 import Day6


class Day6Test(unittest.TestCase):
    def test_get_total_lanternfish_count_after_days_1(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days(18), 26)

    def test_get_total_lanternfish_count_after_days_2(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days(80), 5934)

    def test_get_total_lanternfish_count_after_days_3(self):
        d = Day6('day6_input2.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days(80), 351092)

    def test_get_total_lanternfish_count_after_days2_2(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days2(18), 26)

    def test_get_total_lanternfish_count_after_days2_3(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days2(80), 5934)

    def test_get_total_lanternfish_count_after_days3_0(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days3(18), 26)

    def test_get_total_lanternfish_count_after_days3_1(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days3(80), 5934)

    def test_get_total_lanternfish_count_after_days3_2(self):
        d = Day6('day6_input2.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days3(80), 351092)

    def test_get_total_lanternfish_count_after_days4_0(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days4(80), 5934)

    def test_get_total_lanternfish_count_after_days4_1(self):
        d = Day6('day6_input2.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days4(80), 351092)

    def test_get_total_lanternfish_count_after_days5_1(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days5(18), 26)

    def test_get_total_lanternfish_count_after_days5_2(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days5(80), 5934)

    def test_get_total_lanternfish_count_after_days5_3(self):
        d = Day6('day6_input2.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days5(80), 351092)

    def test_get_total_lanternfish_count_after_days5_4(self):
        d = Day6('day6_input1.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days5(256), 26984457539)

    def test_get_total_lanternfish_count_after_days5_5(self):
        d = Day6('day6_input2.txt')

        self.assertEqual(d.get_total_lanternfish_count_after_days5(256), 26984457539)

    if __name__ == '__main__':
        unittest.main()