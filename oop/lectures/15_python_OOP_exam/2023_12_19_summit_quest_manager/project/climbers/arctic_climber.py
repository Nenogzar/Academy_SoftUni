from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    MIN_STRENGHTH = 100
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGHTH

    def climb(self, peak: BasePeak):
        reduced_amount = {"Extreme": [20, 2],
                          "Advanced": [20, 1.5]}

        peak_lvl = peak.difficulty_level
        self.strength -= reduced_amount[peak_lvl][0] * reduced_amount[peak_lvl][1]
        self.conquered_peaks.append(peak.name)
        return peak_lvl
