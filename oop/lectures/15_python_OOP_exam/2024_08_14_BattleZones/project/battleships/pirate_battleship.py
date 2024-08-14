from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    BASE_AMMUNITION = 80
    REDUCE_AMMUNITION = 10

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.BASE_AMMUNITION)

    def attack(self):
        self.ammunition = max(self.ammunition - self.REDUCE_AMMUNITION, 0)
