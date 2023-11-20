# Code smell
class Statistics:
    def calc_max(self, values):
        self.max = np.max(values)

    def calc_min(self, values):
        self.min = np.min(values)

if __name__ == '__main__':
    stats = Statistics()
    print(stats.max, stats.min)  # Raises an AttributeError
    stats.calc_max([0, 1, 5, -3])
    stats.calc_min([0, 1, 5, -3])
    print(stats.max, stats.min)

# Better
class Statistics:
    def __init__(self, values):
        self.values = values

    @property
    def max(self):
        return np.max(self.values)

    @property
    def min(self):
        return np.min(self.values)


if __name__ == '__main__':
    stats = Statistics([0, 1, 5, -3])
    print(stats.max, stats.min)
    stats.values = [1, 2, 3]
    print(stats.max, stats.min)