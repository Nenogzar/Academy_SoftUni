from project.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.50
    def __init__(self, name: str, portion: float,brand: str):
        super().__init__(name, portion, self.PRICE, brand)



# try:
#     BT = Tea(name="Black Tea", portion=500, brand="Lord Nelson")
#     print(repr(BT))
# except ValueError as e:
#     print(e)

# #  - Black Tea Lord Nelson - 500.00ml - 2.50lv
