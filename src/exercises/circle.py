class Circle:

    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.numberOfContainingPoints = 0

    def contains(self, x: int, y: int):
        result: bool = (x - self.x)*(x - self.x) + (y - self.y)*(y - self.y) <= self.radius*self.radius
        if result == True:
            self.numberOfContainingPoints =+ 1

        return result

    def count_containing_points(self, x_coords, y_coords):
        number_of_containing_points = 0
        for x, y in zip(x_coords, y_coords):
            self.contains(x, y)
        return number_of_containing_points
