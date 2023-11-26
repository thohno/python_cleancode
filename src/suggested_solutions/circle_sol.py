import numpy as np


class Circle:

    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.numberOfContainingPoints = 0

    def contains(self, x: int, y: int):
        is_in_circle = self.is_within_circle(x, y)
        if is_in_circle:
            self.numberOfContainingPoints += 1
        return is_in_circle

    def is_within_circle(self, x, y):
        x_distance = (x - self.x)
        y_distance = (y - self.y)
        return self.square(x_distance) + self.square(y_distance) <= self.square(self.radius)

    def square(self, value):
        return np.square(value)

    def count_containing_points(self, x_coords, y_coords):
        number_of_containing_points = 0
        for x, y in zip(x_coords, y_coords):
            self.contains(x, y)
        return number_of_containing_points
