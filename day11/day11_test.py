import unittest
from day11 import Day11


class Day11Test(unittest.TestCase):
    def test_total_flashes_0(self):
        d = Day11('day11_input0.txt')

        self.assertEqual(d.total_flashes(1), 9)

    def test_total_flashes_1(self):
        d = Day11('day11_input1.txt')

        self.assertEqual(d.total_flashes(10), 204)

    def test_total_flashes_2(self):
        d = Day11('day11_input1.txt')

        self.assertEqual(d.total_flashes(100), 1656)

    def test_total_flashes_3(self):
        d = Day11('day11_input2.txt')

        self.assertEqual(d.total_flashes(100), 1717)

    def test_first_step_which_all_flash_1(self):
        d = Day11('day11_input1.txt')

        self.assertEqual(d.first_step_which_all_flash(), 195)

    def test_first_step_which_all_flash_2(self):
        d = Day11('day11_input2.txt')

        self.assertEqual(d.first_step_which_all_flash(), 476)

    if __name__ == '__main__':
        unittest.main()