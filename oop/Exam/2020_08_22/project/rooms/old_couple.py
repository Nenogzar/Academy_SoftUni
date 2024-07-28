from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        self.member_in_room = 2
        self.room_cost = 15
        super().__init__(family_name, pension_one + pension_two, self.member_in_room)
        self.appliances = [TV(), Fridge(), Stove()] * self.member_in_room
        self.calculate_expenses(self.appliances)
