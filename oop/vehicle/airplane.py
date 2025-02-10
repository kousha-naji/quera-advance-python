from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle


class Airplane(GroundVehicle, FlyingVehicle):
    def __init__(self, airline, number_of_crew, captain, **kwargs):
        super().__init__(**kwargs)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


airplaine = Airplane(airline='iranair', number_of_crew=3, captain='koosha', number_of_seats=200, number_of_wheels=10
                     , steering_wheel=20, max_speed=499, price=40000000, name='ali', )