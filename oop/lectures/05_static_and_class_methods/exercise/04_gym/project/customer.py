from project.base_entity import BaseEntity


class Customer(BaseEntity):
    # _id_counter = 1  # Специализиран брояч за Customer

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
