from project.booths.booth import Booth


class OpenBooth(Booth):
    price_per_person = 2.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self,number_of_people: int):
        self.price_for_reservation = number_of_people * self.price_per_person
        self.is_reserved = True


