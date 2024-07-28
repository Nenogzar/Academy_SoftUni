from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        self.member_in_room = 1
        self.room_cost = 10
        super().__init__(family_name, salary, self.member_in_room)
        self.appliances = [TV()] * self.member_in_room
        self.calculate_expenses(self.appliances)
