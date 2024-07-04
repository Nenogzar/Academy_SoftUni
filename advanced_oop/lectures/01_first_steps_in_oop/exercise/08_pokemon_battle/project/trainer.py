from typing import List


class Trainer:

    def __init__(self, name:str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_obj):
        if pokemon_obj in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon_obj)
        return f"Caught {pokemon_obj.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        # Option 1 -> fast but long
        # pokemon = None
        #
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         pokemon = p
        #         break

        # Option 2 -> slow, but short
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return "Pokemon is not caught"

        # Option 3 -> fast and short
        
        try:
            pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"

        except StopIteration:
            return "Pokemon is not caught"

    def trainer_data(self):
        message = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        message += "\n".join(f"- {p.pokemon_details()}" for p in self.pokemons)
        return message
