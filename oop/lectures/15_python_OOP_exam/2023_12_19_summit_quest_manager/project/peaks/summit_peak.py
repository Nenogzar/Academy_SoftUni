from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    EXTREME_LEVEL = 2500
    ADVANCE_LEVEL_MIN = 1500
    ADVANCE_LEVEL_MAX = 2500

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > self.EXTREME_LEVEL:
            return "Extreme"
        elif self.ADVANCE_LEVEL_MIN <= self.elevation <= self.ADVANCE_LEVEL_MAX:
            return "Advanced"
