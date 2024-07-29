from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    member_in_room = 1
    room_cost = 10
    appliance = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.member_in_room)
        self.appliances = self.appliance  * self.member_in_room
        self.calculate_expenses(self.appliances)
