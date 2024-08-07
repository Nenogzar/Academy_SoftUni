class Validation:

    @staticmethod
    def valid_phone_number(number, length, message):
        if not (number[0] == '0' and len(number) == length and number.isdigit()):
            raise ValueError(message)

    @staticmethod
    def valid_not_empty_string(name, message):
        if name == "" or name.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_price(price, message):
        if price <= 0.00:
            raise ValueError(message)

    @staticmethod
    def duplicate_phone_number(number: str, number_list: [], message: str):
        if any(ph.phone_number == number for ph in number_list):
            raise Exception(message)

    @staticmethod
    def five_items_in_menu(menu: [], message: str):
        if len(menu) < 5:
            raise Exception(message)

    @staticmethod
    def valid_meal(order_meal: dict, app_meal: dict):
        for m in order_meal:
            if m not in app_meal:
                raise Exception(f"{m} is not on the menu!")

    @staticmethod
    def valid_meal_quantity(order_meal: dict, app_meal: dict):
        for meal, quantity in order_meal.items():
            if app_meal[meal].quantity < quantity:
                raise Exception(f"Not enough quantity of {app_meal[meal].__class__.__name__}: {meal}!")


    @staticmethod
    def order_meals(meals: []):
        if not meals:
            raise Exception("There are no ordered meals!")
