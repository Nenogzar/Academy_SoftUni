class ExercisePlan:
    id = 1  # Class attribute for auto-incrementing IDs

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id
        ExercisePlan.id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self) -> str:
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def get_next_id(cls) -> int:
        return cls.id
