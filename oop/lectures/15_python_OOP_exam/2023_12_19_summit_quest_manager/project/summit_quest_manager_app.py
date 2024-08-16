from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    @property
    def valid_climber_type(self):
        return {"ArcticClimber": ArcticClimber,
                "SummitClimber": SummitClimber}

    @property
    def valid_peak_type(self):
        return {"ArcticPeak": ArcticPeak,
                "SummitPeak": SummitPeak}

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.valid_climber_type:
            return f"{climber_type} doesn't exist in our register."

        if any(c.name == climber_name for c in self.climbers):
            return f"{climber_name} has been already registered."

        new_climber = self.valid_climber_type[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.valid_peak_type:
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.valid_peak_type[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        current_peak = next(p for p in self.peaks if peak_name == p.name)
        current_climber = next(c for c in self.climbers if climber_name == c.name)
        items = current_peak.get_recommended_gear()

        missing_gear = set(items) - set(gear)

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            current_climber.is_prepared = False
            missing_gear_list = sorted(missing_gear)
            missing_gear_str = ', '.join(missing_gear_list)
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {missing_gear_str}."


    def perform_climbing(self, climber_name: str, peak_name: str):
        current_peak = next((p for p in self.peaks if peak_name == p.name), None)
        if not current_peak:
            return f"Peak {peak_name} is not part of the wish list."


        current_climber = next((c for c in self.climbers if climber_name == c.name), None)
        if not current_climber:
            return f"Climber {climber_name} is not registered yet."


        if current_climber.is_prepared and current_climber.can_climb():
            return f"{climber_name} conquered {peak_name} whose difficulty level is {current_climber.climb(current_peak)}."

        if not current_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        current_climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."




    def get_statistics(self):
        # Филтрираме катерачите, които са покорили поне един връх
        climbers_with_peaks = [c for c in self.climbers if c.conquered_peaks]

        # Сортираме катерачите по брой покорени върхове (низходящо) и по име (азбучен ред)
        sorted_climbers = sorted(
            climbers_with_peaks,
            key=lambda c: (-len(c.conquered_peaks), c.name)
        )

        # Общ брой уникални покорени върхове
        unique_peaks = set()
        for climber in sorted_climbers:
            unique_peaks.update(climber.conquered_peaks)
        total_climbed_peaks = len(unique_peaks)

        # Форматираме статистиката на катерачите
        climber_statistics = '\n'.join(str(climber) for climber in sorted_climbers)

        # Форматираме и връщаме резултата
        return (f"Total climbed peaks: {total_climbed_peaks}\n"
                "**Climber's statistics:**\n"
                f"{climber_statistics}")



