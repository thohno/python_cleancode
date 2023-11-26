import unittest

from src.exercises.circle import Circle
from src.exercises.shapegroup import ShapeGroup


class TestShapeGroup(unittest.TestCase):

    def test_add_withReadOnly(self):
        shape_group = ShapeGroup()
        shape_group.read_only = True

        shape_group.add(Circle(0, 0, 0))

        self.assertEqual(0, shape_group.size)

    def test_add_withoutReadOnly(self):
        shape_group = ShapeGroup()
        shape_group.read_only = False

        shape_group.add(Circle(0, 0, 0))

        self.assertEqual(1, shape_group.size)

    def test_add_sameElementTwice(self):
        shape_group = ShapeGroup()
        shape_group.read_only = False

        circle = Circle(0, 0, 0)
        shape_group.add(circle)
        shape_group.add(circle)

        self.assertEqual(1, shape_group.size)

    def test_add_internalArraySizeExceeded(self):
        shape_group = ShapeGroup()
        shape_group.read_only = False

        for i in range(11):
            shape_group.add(Circle(0, 0, 0))

        self.assertEqual(11, shape_group.size)
