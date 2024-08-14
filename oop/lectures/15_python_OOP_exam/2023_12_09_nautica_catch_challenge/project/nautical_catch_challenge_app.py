from typing import List
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    @property
    def valid_divers_type(self):
        return {"FreeDiver": FreeDiver,
                "ScubaDiver": ScubaDiver}

    @property
    def valid_fish_type(self):
        return {"PredatoryFish": PredatoryFish,
                "DeepSeaFish": DeepSeaFish}

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.valid_divers_type:
            return f"{diver_type} is not allowed in our competition."

        if any(d.name == diver_name for d in self.divers):
            return f"{diver_name} is already a participant."

        new_diver = self.valid_divers_type[diver_type](diver_name)
        self.divers.append(new_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.valid_fish_type:
            return f"{fish_type} is forbidden for chasing in our competition."

        if any(f.name == fish_name for f in self.fish_list):
            return f"{fish_name} is already permitted."

        new_fish = self.valid_fish_type[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        fish = next((f for f in self.fish_list if f.name == fish_name), None)

        if not diver:
            return f"{diver_name} is not registered for the competition."
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count_divers = 0
        divers = [d for d in self.divers if d.has_health_issue == True]

        for d in divers:
            d.update_health_status()
            d.renew_oxy()
            count_divers += 1

        return f"Divers recovered: {count_divers}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)

        output = [f"**{diver_name} Catch Report**", ]
        for fish in diver.catch:
            output.append(fish.fish_details())

        return "\n".join(output)


    def competition_statistics(self):
        output = ["**Nautical Catch Challenge Statistics**", ]

        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        for diver in sorted_divers:
            if diver.has_health_issue:
                continue

            output.append(diver.__str__())

        return "\n".join(output)

