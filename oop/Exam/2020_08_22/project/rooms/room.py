
class Room:
    room_cost = 0

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []  # contain all kids in that room (objects)
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        expense = 0
        for arg in args:
            for ex in arg:
                expense += ex.get_monthly_expense()
        self.__expenses = expense

    @property
    def monthly_total_cost(self):
        return self.__expenses + self.room_cost