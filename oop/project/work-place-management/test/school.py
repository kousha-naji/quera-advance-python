from work_place import WorkPlace, Consts
from math import sqrt, floor


class School(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.costs = None
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = floor(sqrt(self.level))

    def calc_costs(self):
        self.costs = Consts.BASE_PLACE_COST * floor(sqrt(self.level))
        return self.costs
