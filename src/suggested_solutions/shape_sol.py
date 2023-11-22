# Conditional complexity
# Deeply nested control flow

import numpy as np


class Shape:
    def __init__(self):
        self.size = 0
        self.shapes = np.full(5, None, dtype=object)
        self.readOnly = False

    def add(self, shape):
        if self.readOnly or self.contains(shape):
            return

        if self.shouldGrow():
            self.grow()

        self.addToShapes(shape)

    def contains(self, shape):
        return self.shape in self.shapes

    def addToShapes(self, shape):
        self.shapes[self.size] = shape
        self.size += 1

    def grow(self):
        newShapes = np.zeros(len(self.shapes) + 10)
        for i in range(self.size):
            newShapes[i] = self.shapes[i]
        self.shapes = newShapes

    def shouldGrow(self):
        return self.size + 1 > len(self.shapes)


if __name__ == '__main__':
    pass