# Conditional complexity
# Deeply nested control flow

import numpy as np


class ShapeGroup:
    def __init__(self):
        self.size = 0
        self.shapes = np.full(5, None, dtype=object)
        self.read_only = False

    def add(self, shape):
        if self.read_only or self.contains(shape):
            return

        if self.should_grow():
            self.grow()

        self.add_to_shapes(shape)

    def contains(self, shape):
        return shape in self.shapes

    def add_to_shapes(self, shape):
        self.shapes[self.size] = shape
        self.size += 1

    def grow(self):
        new_shapes = np.full(len(self.shapes) + 10, None, dtype=object)
        for i in range(self.size):
            new_shapes[i] = self.shapes[i]
        self.shapes = new_shapes

    def should_grow(self):
        return self.size + 1 > len(self.shapes)

    @property
    def read_only(self):
        return self.read_only

    @read_only.setter
    def read_only(self, read_only):
        self.read_only = read_only


if __name__ == '__main__':
    pass
