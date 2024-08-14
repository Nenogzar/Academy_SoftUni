from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120
    REDUCE_PERCENT = 0.6

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduction = round(self.oxygen_level - (time_to_catch * self.REDUCE_PERCENT))

        if reduction < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = reduction

        if self.oxygen_level >= 0:
            self.update_health_status()

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL
