# Identify the code smells from the following list:
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


class ShapeGroup:

    def __init__(self):
        self.shapes = np.empty(10, dtype=object)
        self.size = 0
        self.read_only = False

    def add(self, shape):
        if not self.read_only:
            if not self.contains(shape):
                new_size = self.size + 1
                if new_size > len(self.shapes):
                    new_shapes = np.empty(len(self.shapes) + 10, dtype=object)
                    i = 0
                    while i < self.size:
                        new_shapes[i] = self.shapes[i]
                        i += 1
                    self.shapes = new_shapes
                self.shapes[self.size] = shape
                self.size += 1
                return
            return

    def contains(self, shape):
        return shape in self.shapes

    @property
    def read_only(self):
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        self._read_only = read_only
