class Package:
    def __init__(self, weight: float, distance: float):
        if weight < 0:
            raise ValueError("Invalid weight!")
        self.weight = weight
        self.distance = distance