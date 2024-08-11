from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    EQUIPMENT_PROTECTION = 120
    EQUIPMENT_PRICE = 15
    INCREASES_PRICE = 0.2

    def __init__(self):
        super().__init__(self.EQUIPMENT_PROTECTION, self.EQUIPMENT_PRICE)

    def increase_price(self):
        self.price *= (1 + self.INCREASES_PRICE)
