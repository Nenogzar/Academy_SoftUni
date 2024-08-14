from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone

class BattleManager:
    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    @property
    def valid_types_zones(self):
        return {"RoyalZone": RoyalZone,
                "PirateZone": PirateZone}

    @property
    def valid_types_battleship(self):
        return {'RoyalBattleship': RoyalBattleship,
                'PirateBattleship': PirateBattleship}

    @property
    def attack_rules(self):
        return {
            (RoyalZone, PirateBattleship): False,
            (PirateZone, RoyalBattleship): False
        }

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.valid_types_zones:
            raise Exception("Invalid zone type!")

        if any(z for z in self.zones if z.code == zone_code):
            raise Exception("Zone already exists!")

        new_zone = self.valid_types_zones[zone_type](zone_code)
        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.valid_types_battleship:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        new_ship = self.valid_types_battleship[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if len(zone.ships) >= zone.volume:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        # Определяме правилото за текущата зона и кораб
        ship_type = type(ship)
        zone_type = type(zone)
        is_attacking = self.attack_rules.get((zone_type, ship_type), True)

        ship.is_attacking = is_attacking

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if ship is None:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]

        if len(attackers) < 1 or len(targets) < 1:
            return "Not enough participants. The battle is canceled."

        zone_type = type(zone).__name__
        attacking_ships = [s for s in attackers if type(s).__name__.replace("Battleship", "Zone") == zone_type]
        if not attacking_ships:
            return "No valid attacker found. The battle is canceled."

        most_powerful_attacker = max(attacking_ships, key=lambda s: s.hit_strength)

        enemy_ships = [s for s in targets if type(s).__name__.replace("Battleship", "Zone") != zone_type]
        if not enemy_ships:
            return "No valid target found. The battle is canceled."

        healthiest_target = max(enemy_ships, key=lambda s: s.health)

        healthiest_target.take_damage(most_powerful_attacker)
        most_powerful_attacker.attack()

        if healthiest_target.health <= 0:
            zone.ships.remove(healthiest_target)
            self.ships.remove(healthiest_target)
            return f"{healthiest_target.name} lost the battle and was sunk."

        if most_powerful_attacker.ammunition <= 0:
            zone.ships.remove(most_powerful_attacker)
            self.ships.remove(most_powerful_attacker)
            return f"{most_powerful_attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ships_count = len(available_ships)

        available_ships_names = ", ".join(ship.name for ship in available_ships) if available_ships else ""

        sorted_zones = sorted(self.zones, key=lambda z: z.code)
        zones_info = [zone.zone_info() for zone in sorted_zones]

        result = [
            f"Available Battleships: {available_ships_count}",
            f"#{available_ships_names}#",
            "***Zones Statistics:***",
            f"Total Zones: {len(sorted_zones)}"
        ]

        result.extend(zones_info)

        return "\n".join(line for line in result if line)
