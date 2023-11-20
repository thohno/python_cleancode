# Code smell
class Statistics:
    def __init__(self):
        pass

    def calc_max(self, values):
        self.values = values
        self.max = np.max(self.values)

    def calc_min(self):
        self.min = np.min(self.values)


if __name__ == '__main__':
    stats = Statistics()
    calc_max([0, 1, 5, -3])
    calc_min()
    print(stats.max, stats.min)

# Better
class Statistics:
    def __init__(self, values):
        self.values = values

    def calc_max(self):
        return np.max(self.values)

    def calc_min(self):
        return np.min(self.values)


if __name__ == '__main__':
    stats = Statistics([0, 1, 5, -3])
    print(stats.calc_max(), stats.calc_min())