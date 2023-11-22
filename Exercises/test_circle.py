import unittest

from Exercises.circle import Circle


class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(x=0, y=0, radius=1)

    def test_contains_point(self):
        self.assertTrue(self.circle.contains(0, 0))
        self.assertTrue(self.circle.contains(0, 1))
        self.assertTrue(self.circle.contains(1, 0))

    def test_not_contains_point(self):
        self.assertFalse(self.circle.contains(1, 1))
        self.assertFalse(self.circle.contains(-1, -1))
        self.assertFalse(self.circle.contains(1, -1))
        self.assertFalse(self.circle.contains(-1, 1))

    def test_add_same_point(self):
        self.assertFalse(self.circle.contains(11, 11))



