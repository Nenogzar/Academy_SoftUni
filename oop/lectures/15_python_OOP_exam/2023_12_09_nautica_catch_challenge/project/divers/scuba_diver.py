from project.divers.base_diver import BaseDiver

class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    REDUCE_PERCENT = 0.3

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
