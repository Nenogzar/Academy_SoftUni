from typing import List

from project.client import Client
from project.meals.meal import Meal
from project.validation.validation import Validation


class FoodOrdersApp:

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.receipt_it = 0

    @property
    def valid_meals(self):
        return "Starter", "MainDish", "Dessert"

    def __return_client(self, client_phone_number: str):
        for cl in self.clients_list:
            if cl.phone_number == client_phone_number:
                return cl
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return new_client

    def __get_menu(self):
        return {m.name: m for m in self.menu}

    def register_client(self, client_phone_number: str):
        Validation.duplicate_phone_number(client_phone_number, self.clients_list,
                                          "The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for m in meals:
            if m.__class__.__name__ in self.valid_meals:
                self.menu.append(m)
        # [self.menu.append(m) for m in meals if m.__class__.__name__ in self.valid_meals]

    def show_menu(self):
        Validation.five_items_in_menu(self.menu, "The menu is not ready!")

        # return "\n".join(m.details() for m in self.menu)
        return "\n".join(map(lambda m: m.details(), self.menu))

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Validation.five_items_in_menu(self.menu, "The menu is not ready!")
        client = self.__return_client(client_phone_number)
        menu_order = self.__get_menu()

        Validation.valid_meal(meal_names_and_quantities, menu_order)
        Validation.valid_meal_quantity(meal_names_and_quantities, menu_order)

        for mean, quantity in meal_names_and_quantities.items():
            menu_order[mean].quantity -= quantity
            client.shopping_cart.append(menu_order[mean])

        client.bill += sum(menu_order[mean].price * qty for mean, qty in meal_names_and_quantities.items())
        client.order.update(meal_names_and_quantities)

        return f"Client {client_phone_number} successfully ordered {', '.join(client.order)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__return_client(client_phone_number)
        menu_order = self.__get_menu()
        Validation.order_meals(client.shopping_cart)

        for mean, quantity in client.order.items():
            menu_order[mean].quantity += quantity

        client.reset_client_order()
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__return_client(client_phone_number)
        Validation.order_meals(client.shopping_cart)

        bill = client.bill
        client.reset_client_order()
        self.receipt_it += 1
        return f"Receipt #{self.receipt_it} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
