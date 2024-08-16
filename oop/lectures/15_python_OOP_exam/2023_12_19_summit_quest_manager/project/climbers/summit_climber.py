from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    MIN_STRENGHTH = 75
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGHTH

    def climb(self, peak: BasePeak):
        reduced_amount = {"Extreme": [30, 2.5],
                          "Advanced": [30, 1.3]}

        peak_lvl = peak.difficulty_level
        self.strength -= reduced_amount[peak_lvl][0] * reduced_amount[peak_lvl][1]
        self.conquered_peaks.append(peak.name)
        return peak_lvl

