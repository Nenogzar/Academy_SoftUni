from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)

        if dvd is None or customer is None:
            return "Invalid customer or DVD"

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in customer.rented_dvds if d.id == dvd_id), None)

        if dvd is None or customer is None:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers_repr = "\n".join(str(customer) for customer in self.customers)
        dvds_repr = "\n".join(str(dvd) for dvd in self.dvds)
        return customers_repr + "\n" + dvds_repr