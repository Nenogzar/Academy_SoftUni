from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    EXTREME_LEVEL = 3000
    ADVANCE_LEVEL_MIN = 2000
    ADVANCE_LEVEL_MAX = 3000

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > self.EXTREME_LEVEL:
            return "Extreme"
        elif self.ADVANCE_LEVEL_MIN <= self.elevation <= self.ADVANCE_LEVEL_MAX:
            return "Advanced"
