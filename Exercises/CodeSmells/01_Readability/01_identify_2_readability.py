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


class Shape:
    def __init__(self):
        self.size = 0
        self.shapes = np.zeros(5)
        self.readOnly = False

    def add(self, shape):
        if not self.readOnly:
            if not self.contains(shape):
                newSize = self.size + 1
                if newSize > len(self.shapes):
                    newShapes = np.zeros(len(self.shapes) + 10)
                    for i in range(self.size):
                        newShapes[i] = self.shapes[i]
                    shapes = newShapes
                shapes[self.size] = shape
                self.size += 1
                return
            return

    def contains(self, shape):
        return self.shape in self.shapes


if __name__ == '__main__':
    pass