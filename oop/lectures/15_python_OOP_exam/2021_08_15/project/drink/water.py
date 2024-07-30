from project.drink.drink import Drink


class Water(Drink):
    PRICE = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.PRICE, brand)

# try:
#     water = Water(name="Mineral Water", portion=500, brand="Bankya")
#     print(repr(water))
# except ValueError as e:
#     print(e)
# #  - Mineral Water Bankya - 500.00ml - 1.50lv
