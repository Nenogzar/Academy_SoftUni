from typing import List
from project.player import Player
from project.supply.supply import Supply
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    @property
    def type_sustain(self):
        return {"Food": Food,
                "Drink": Drink}

    def add_player(self, *args):
        successfully_added = []
        for player in args:
            if player.name not in [p.name for p in self.players]:
                self.players.append(player)
                successfully_added.append(player.name)
        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *supply):
        for sup in supply:
            self.supplies.append(sup)

    def sustain(self, player_name: str, sustenance_type: str):
        if player_name not in [p.name for p in self.players]:
            return

        if sustenance_type not in self.type_sustain:
            return

        player = next(p for p in self.players if p.name == player_name)

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply_class = self.type_sustain[sustenance_type]
        supplies_of_type = [s for s in self.supplies if isinstance(s, supply_class)]

        if not supplies_of_type:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        supply_to_use = supplies_of_type[-1]
        player.stamina = min(100, player.stamina + supply_to_use.energy)
        self.supplies.remove(supply_to_use)

        return f"{player_name} sustained successfully with {supply_to_use.name}."


    def duel(self, first_player_name: str, second_player_name: str):
        first_player = next(p for p in self.players if p.name == first_player_name)
        second_player = next(p for p in self.players if p.name == second_player_name)

        messages = []

        if first_player.stamina == 0 and second_player.stamina == 0:
            messages.append(f"Player {first_player_name} does not have enough stamina.")
            messages.append(f"Player {second_player_name} does not have enough stamina.")
            return '\n'.join(messages)

        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            attacker, defender = first_player, second_player
        else:
            attacker, defender = second_player, first_player

        # First attack
        if defender.stamina - (attacker.stamina / 2) <= 0:
            defender.stamina = 0  # Set to 0 instead of negative value
            return f"Winner: {attacker.name}"
        else:
            defender.stamina -= attacker.stamina / 2

        # Second attack
        if attacker.stamina -(defender.stamina / 2) <= 0:
            attacker.stamina = 0  # Set to 0 instead of negative value
            return f"Winner: {defender.name}"
        else:
            attacker.stamina -= defender.stamina / 2

        # Determine winner
        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"


    def next_day(self):
        # Reduce stamina by age * 2 for each player
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        # Sustain each player with one food and one drink
        for player in self.players:
            if player.need_sustenance:
                try:
                    # Try to give food first
                    self.sustain(player.name, "Food")
                except Exception as e:
                    print(e)
                try:
                    # Then try to give drink
                    self.sustain(player.name, "Drink")
                except Exception as e:
                    print(e)


    def __str__(self):
        result = []
        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")

        for supply in self.supplies:
            result.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")

        return "\n".join(result)
