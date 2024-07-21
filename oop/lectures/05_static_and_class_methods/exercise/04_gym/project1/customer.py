class Customer:
    id = 1  # Class attribute for auto-incrementing IDs

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id
        Customer.id += 1

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @classmethod
    def get_next_id(cls) -> int:
        return cls.id
