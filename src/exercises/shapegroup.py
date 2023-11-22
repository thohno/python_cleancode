# Identify the 2 code smells from the following list:
# Long methods
# Bad & redundant comments
# Bad variable/method naming
# Too many function arguments
# Conditional complexity
# Deeply nested control flow
# Cyclomatic complexity
# Temporary fields
# Side effects

import numpy as np
import self


class ShapeGroup:

    def __init__(self):
        self.size = 0
        self.shapes = np.zeros(5)
        self.read_only = False

    def add(self, shape):
        if not self.read_only:
            if not self.contains(shape):
                newSize = self.size + 1
                if newSize > len(self.shapes):
                    newShapes = np.zeros(len(self.shapes) + 10)
                    i = 0
                    while i < self.size:
                        newShapes[i] = self.shapes[i]
                        i += 1
                    shapes = newShapes
                shapes[self.size] = shape
                self.size += 1
                return
            return

    def contains(self, shape):
        return self.shape in self.shapes

    @property
    def read_only(self):
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        self._read_only = read_only