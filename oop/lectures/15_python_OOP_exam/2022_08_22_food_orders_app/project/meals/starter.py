from project.meals.meal import Meal


class Starter(Meal):
    _default_quantity = 60

    def __init__(self, name: str, price: float, quantity: int = _default_quantity):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
