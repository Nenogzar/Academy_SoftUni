from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.validation.validation import Validation


class HorseRaceApp:
    horse_classes = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in self.horse_classes:
            return

        # Създаване на коня въз основа на типа чрез речника
        horse_class = self.horse_classes[horse_type]
        new_horse = horse_class(horse_name, horse_speed)
        self.horses.append(new_horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        if any(race.race_type == race_type for race in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        curr_jockey, curr_horse = None, None

        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                curr_horse = horse
                break

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                curr_jockey = jockey
                break

        if not curr_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not curr_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if curr_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        curr_horse.is_taken = True
        curr_jockey.horse = curr_horse
        return f"Jockey {jockey_name} will ride the horse {curr_jockey.horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")


        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")


        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")


        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."


        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        # Проверка дали съществува състезание
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        # Проверка за минимум участници
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        # Намиране на победителя
        winner_jockey = None
        highest_speed = -1

        for jockey in race.jockeys:
            if jockey.horse and jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner_jockey = jockey

        if winner_jockey is None:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        return (f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is "
                f"{winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}.")

