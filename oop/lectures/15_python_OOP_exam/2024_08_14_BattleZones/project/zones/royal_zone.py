from project.zones.base_zone import BaseZone
from project.battleships.pirate_battleship import PirateBattleship

class RoyalZone(BaseZone):
    BASE_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.BASE_VOLUME)

    def zone_info(self):
        battleships_total_count = len(self.ships)
        pirateships_count = sum(1 for ship in self.get_ships() if isinstance(ship, PirateBattleship))

        sorted_ships = self.get_ships()
        battleship_names = ", ".join(ship.name for ship in sorted_ships)

        info = (f"@Royal Zone Statistics@\n"
                f"Code: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Royal Zone: {battleships_total_count}, "
                f"{pirateships_count} out of them are Pirate Battleships.")

        if battleship_names:
            info += f"\n#{battleship_names}#"

        return info
