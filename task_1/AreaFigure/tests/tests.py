import unittest
from AreaFigure.AreaFigure.calculate_areas import Circle, Triangle
from math import pi

class TestFigures(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        True_area = round(pi * 5 ** 2, 2)
        self.assertAlmostEqual(circle.calculate_area(), True_area, delta=0.01)

    def test_triangle_area(self):
        triangle = Triangle(side1=3, side2=4, side3=5)
        True_area = 6.0
        self.assertAlmostEqual(triangle.calculate_area(), True_area, delta=0.01)

    def test_is_rectangular_true(self):
        rectangular_triangle = Triangle(side1=3, side2=4, side3=5)
        self.assertTrue(rectangular_triangle.is_rectangular())

    def test_is_rectangular_false(self):
        non_rectangular_triangle = Triangle(side1=3, side2=4, side3=6)
        self.assertFalse(non_rectangular_triangle.is_rectangular())

if __name__ == '__main__':
    unittest.main()

