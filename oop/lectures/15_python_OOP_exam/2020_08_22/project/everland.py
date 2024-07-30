from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []
        self.total_population = 0

    def add_room(self, room: Room):
        self.rooms.append(room)
        self.total_population += room.members_count

    def get_monthly_consumptions(self):
        return f"Monthly consumtions: {sum(r.monthly_total_cost for r in self.rooms):.2f}$."

    def pay(self):
        if_not_budget, rooms_remove = [], []
        for room in self.rooms:
            pay_out = room.room_cost + room.expenses
            if pay_out > room.budget:
                if_not_budget.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_remove.append(self.rooms.index(room))
                continue

            room.budget -= pay_out
            if_not_budget.append(f"{room.family_name} paid"
                                 f" {room.expenses + room.room_cost:.2f}$"
                                 f" and have {room.budget:.2f}$ left.")
        if rooms_remove:
            for _ in range(len(self.rooms) - 1, -1, -1):
                self.rooms.pop(rooms_remove.pop())
        return '\n'.join(if_not_budget)

    def status(self):
        result = []
        total_population = sum(people.members_count for people in self.rooms)
        result.append(f"Total population: {total_population}")
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members."
                          f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            for child, info in enumerate(room.children, 1):
                result.append(f"--- Child {child} monthly cost: {info.get_monthly_expense():.2f}$")
            result.append(f"--- Appliances monthly cost: {sum(r.get_monthly_expense() for r in room.appliances):.2f}$")
        return '\n'.join(result)


# ####################################################################
#
everland = Everland()


# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
# if __name__ == "__main__":
#     test_one()



#
# young_couple = YoungCouple("Johnsons", 150, 205)
#
# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
# everland.add_room(young_couple)
# everland.add_room(young_couple_with_children)
#
# # Debugging the expenses
# print(f"Johnsons Expected Expenses: 2 * 30 * (1.5 + 1.2 + 1) + 20 = {2 * 30 * (1.5 + 1.2 + 1) + 20}")
# print(f"Peterson Expected Expenses: 4 * 30 * (1.5 + 1.2 + 1) + 30 + 270 + 150 = {4 * 30 * (1.5 + 1.2 + 1) + 30 + 270 + 150}")
#
# print(everland.get_monthly_consumptions())
# print(everland.pay())
# print(everland.status())
