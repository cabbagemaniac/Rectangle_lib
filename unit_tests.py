import unittest
from rectangle import area, perimeter


class RectangleTests(unittest.TestCase):

    def test_area_zero_side(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(5, 10)

    def test_area_non_square(self):
        res = area(4, 9)
        self.assertEqual(res, 36)

    def test_area_square(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_perimeter_zero_side(self):
        res = perimeter(4, 0)
        self.assertEqual(res, 8)

    def test_perimeter_non_square(self):
        res = perimeter(3, 11)
        self.assertEqual(res, 28)

    def test_perimeter_square(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

if __name__ == '__main__':
    unittest.main()