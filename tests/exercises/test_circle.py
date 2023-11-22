import unittest
from parameterized import parameterized

from src.exercises.circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(x=0, y=0, radius=1)

    def test_contains_point(self):
        self.assertTrue(self.circle.contains(0, 0))
        self.assertTrue(self.circle.contains(0, 1))
        self.assertTrue(self.circle.contains(1, 0))

    @parameterized.expand([
        (1, 1, False),
        (-1, -1, False),
        (1, -1, False),
        (-1, 1, False)
    ])
    def test_not_contains_point(self, x, y, expected):
        is_contained = self.circle.contains(x, y)
        self.assertEqual(is_contained, expected)
