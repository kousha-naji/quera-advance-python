from work_place import WorkPlace
from math import sqrt, floor


class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = self.level**2

    def calc_costs(self):
        self.costs = BaseException * floor(sqrt(self.level))
        return self.costs