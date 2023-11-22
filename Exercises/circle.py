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

    def countContainingPoints(self, xCoords, yCoords):
        numberOfContainingPoints = 0
        for x, y in zip(xCoords, yCoords):
            self.contains(x, y)
        return numberOfContainingPoints
