from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        self.member_in_room = 2
        self.room_cost = 20
        super().__init__(family_name, salary_one + salary_two, self.member_in_room)
        self.appliances = [TV(), Fridge(), Laptop()] * self.member_in_room
        self.calculate_expenses(self.appliances)
