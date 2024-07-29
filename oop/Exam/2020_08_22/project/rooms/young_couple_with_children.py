from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    member_in_room = 2
    room_cost = 30
    appliance = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, self.member_in_room + len(children))
        self.children = list(children)
        total_person = self.member_in_room + len(self.children)
        self.appliances = self.appliance * total_person
        self.calculate_expenses(self.children, self.appliance)
