from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    member_in_room = 2
    room_cost = 20
    appliance = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.member_in_room)
        self.appliances = self.appliance * self.member_in_room
        self.calculate_expenses(self.appliances)
