from work_place import WorkPlace, Consts
from math import sqrt, floor


class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.costs = None
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = self.level**2

    def calc_costs(self):
        self.costs = Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level
        return self.costs