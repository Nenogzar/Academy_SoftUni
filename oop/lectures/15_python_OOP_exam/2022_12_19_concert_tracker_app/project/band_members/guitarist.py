from project.band_members.musician import Musician
from project.validation.validation import Validation


class Guitarist(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def posible_skills(self):
        return ["play metal",
                "play rock",
                "read jazz"]

    def learn_new_skill(self, new_skill: str):
        Validation.validate_ganre_or_music(new_skill, self.posible_skills, f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)

        return f"{self.name} learned to {new_skill}."


