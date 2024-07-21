from project.base_entity import BaseEntity

class Equipment(BaseEntity):


    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
