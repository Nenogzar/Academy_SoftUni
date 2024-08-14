from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    BASE_AMMUNITION = 100
    REDUCE_AMMUNITION = 25

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.BASE_AMMUNITION)

    def attack(self):
        self.ammunition = max(self.ammunition - self.REDUCE_AMMUNITION, 0)
