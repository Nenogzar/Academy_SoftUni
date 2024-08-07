from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.valaidation.validation import Validation


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0.0  # represents the total income of the pastry shop

    @property
    def valid_type(self):
        return {"Gingerbread": Gingerbread,
                "Stolen": Stolen}

    @property
    def valid_booth(self):
        return {"Open Booth": OpenBooth,
                "Private Booth": PrivateBooth}

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Validation.validate_type(type_delicacy, self.valid_type, f"{type_delicacy} is not on our delicacy menu!")
        if any(d.name == name for d in self.delicacies):
            raise Exception(f"{name} already exists!")

        new_delicacy = self.valid_type[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Validation.validate_type(type_booth, self.valid_booth, f"{type_booth} is not a valid booth!")
        if any(b.booth_number == booth_number for b in self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        new_booth = self.valid_booth[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)  # Reserve the booth
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(b for b in self.booths if b.booth_number == booth_number)

        total_delicacies_price = sum(d.price for d in booth.delicacy_orders)
        bill = booth.price_for_reservation + total_delicacies_price

        self.income += bill

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
