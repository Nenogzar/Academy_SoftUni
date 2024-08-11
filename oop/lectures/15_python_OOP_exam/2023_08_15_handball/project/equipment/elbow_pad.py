from project.equipment.base_equipment import BaseEquipment


class ElbowPad (BaseEquipment):
    EQUIPMENT_PROTECTION = 90
    EQUIPMENT_PRICE = 25
    INCREASES_PRICE = 0.1

    def __init__(self):
        super().__init__(self.EQUIPMENT_PROTECTION, self.EQUIPMENT_PRICE)

    def increase_price(self):
        self.price *= (1 + self.INCREASES_PRICE)