from person import Person, Consts
from math import floor


class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.income = None
        self.costs = None
        self.price = None
        self.job = "worker"

    def get_price(self):
        self.price = floor((Consts.BASE_PRICE[self.job] * Consts.MIN_AGE) / self.age)
        return self.price

    def calc_life_cost(self):
        self.costs = floor((Consts.BASE_COST[self.job] * Consts.MIN_AGE) / self.age)
        return self.costs

    def calc_income(self):
        self.income = floor((Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * Consts.MIN_AGE) / self.age)
        return self.income