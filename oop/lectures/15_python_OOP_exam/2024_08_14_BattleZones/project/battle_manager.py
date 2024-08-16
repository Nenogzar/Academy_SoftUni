from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in ["RoyalZone", "PirateZone"]:
            raise Exception("Invalid zone type!")
        if any(zone.code == zone_code for zone in self.zones):
            raise Exception("Zone already exists!")
        
        if zone_type == "RoyalZone":
            zone = RoyalZone(zone_code)
        elif zone_type == "PirateZone":
            zone = PirateZone(zone_code)
        
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in ["RoyalBattleship", "PirateBattleship"]:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        if ship_type == "RoyalBattleship":
            ship = RoyalBattleship(name, health, hit_strength)
        elif ship_type == "PirateBattleship":
            ship = PirateBattleship(name, health, hit_strength)

        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if isinstance(zone, RoyalZone) and isinstance(ship, PirateBattleship) or            isinstance(zone, PirateZone) and isinstance(ship, RoyalBattleship):
            ship.is_attacking = False
        else:
            ship.is_attacking = True
        
        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((ship for ship in self.ships if ship.name == ship_name), None)
        if not ship:
            return "No ship with this name!"
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        
        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        if len(zone.ships) < 2:
            return "Not enough participants. The battle is canceled."
        
        attacker = max((ship for ship in zone.ships if ship.is_attacking), key=lambda ship: ship.hit_strength, default=None)
        target = max((ship for ship in zone.ships if not ship.is_attacking), key=lambda ship: ship.health, default=None)

        if not attacker or not target:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        target.take_damage(attacker)

        result = []
        if target.health == 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            result.append(f"{target.name} lost the battle and was sunk.")
        
        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            result.append(f"{attacker.name} ran out of ammunition and leaves.")
        
        if not result:
            result.append("Both ships survived the battle.")
        
        return " ".join(result)

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ships_str = ', '.join(ship.name for ship in available_ships)

        zones_info = '\n'.join(zone.zone_info() for zone in sorted(self.zones, key=lambda z: z.code))

        result = f"Available Battleships: {len(available_ships)}\n"
        if available_ships:
            result += f"#{available_ships_str}#\n"
        result += "***Zones Statistics:***\n"
        result += f"Total Zones: {len(self.zones)}\n"
        result += zones_info

        return result
