import unittest
from day2 import Day2


class Day2Test(unittest.TestCase):
    def test_multiply_horizontal_position_by_depth_1(self):
        d = Day2('day2_input1.txt')
        result = d.multiply_horizontal_position_by_depth()
        self.assertEqual(result, 150)

    def test_multiply_horizontal_position_by_depth_2(self):
        d = Day2('day2_input2.txt')
        result = d.multiply_horizontal_position_by_depth()
        self.assertEqual(result, 1561344)

    def test_advenced_multiply_horizontal_position_by_depth_1(self):
        d = Day2('day2_input1.txt')
        result = d.advenced_multiply_horizontal_position_by_depth()
        self.assertEqual(result, 900)

    def test_advenced_multiply_horizontal_position_by_depth_2(self):
        d = Day2('day2_input2.txt')
        result = d.advenced_multiply_horizontal_position_by_depth()
        self.assertEqual(result, 1848454425)

if __name__ == '__main__':
    unittest.main()
