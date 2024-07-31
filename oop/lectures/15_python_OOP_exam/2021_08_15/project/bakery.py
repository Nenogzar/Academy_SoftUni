from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table
from project.Validators.validators import Validation

class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.validate_non_empty_string(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def __types_food(self):
        return {"Bread": Bread,
                "Cake": Cake
                }

    @property
    def __types_drink(self):
        return {"Tea": Tea,
                "Water": Water
                }

    @property
    def __types_table(self):
        return {"InsideTable": InsideTable,
                "OutsideTable": OutsideTable
                }

    def add_food(self, food_type: str, name: str, price: float):
        Validation.validate_if_exist(name, self.food_menu, f"{food_type} {name} is already in the menu!")

        if food_type in self.__types_food:
            create_food = self.__types_food[food_type](name, price)
            self.food_menu.append(create_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        Validation.validate_if_exist(name, self.drinks_menu, f"{drink_type} {name} is already in the menu!")

        if drink_type in self.__types_drink:
            make_drink = self.__types_drink[drink_type](name, portion, brand)
            self.drinks_menu.append(make_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        Validation.table_duplivaty(table_number,self.tables_repository, f"Table {table_number} is already in the bakery!")

        if table_type in self.__types_table:
            used_table = self.__types_table[table_type](table_number, capacity)
            self.tables_repository.append(used_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):

        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args: str):
        table = next((t for t in self.tables_repository if t.table_number == table_number), None)
        if not table:
            return f"Could not find table {table_number}"

        ordered_foods = []
        missing_foods = []

        for food_name in args:
            food = next((f for f in self.food_menu if f.name == food_name), None)
            if food:
                table.order_food(food)
                ordered_foods.append(food)
            else:
                missing_foods.append(food_name)

        result = [f"Table {table_number} ordered:"]
        result.extend([repr(food) for food in ordered_foods])

        if missing_foods:
            result.append(f"{self.name} does not have in the menu:")
            result.extend(missing_foods)

        return "\n".join(result)

    def order_drink(self, table_number: int, *args: str):
        table = next((t for t in self.tables_repository if t.table_number == table_number), None)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = []
        missing_drinks = []

        for drink_name in args:
            drink = next((d for d in self.drinks_menu if d.name == drink_name), None)
            if drink:
                table.order_drink(drink)
                ordered_drinks.append(drink)
            else:
                missing_drinks.append(drink_name)

        result = [f"Table {table_number} ordered:"]
        result.extend([repr(drink) for drink in ordered_drinks])

        if missing_drinks:
            result.append(f"{self.name} does not have in the menu:")
            result.extend(missing_drinks)

        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = next((t for t in self.tables_repository if t.table_number == table_number), None)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()

            return f"Table: {table_number}\n" \
                   f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
