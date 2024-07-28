from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.member_in_room = 2
        self.room_cost = 30
        super().__init__(family_name, salary_one + salary_two, self.member_in_room + len(children))
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * (self.member_in_room + len(children))
        self.calculate_expenses(self.appliances, self.children)
