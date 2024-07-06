# ******* Classes and Objects - Exercise ******* #

# *******  06_guild_system  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1937#5
You are tasked to create two classes: a Player class and a Guild class.

-project
--player.py
--guild.py
--__init__.py

The Player class should receive a name (string), a hp (int), and a mp (int) upon initialization.

The Player also has 2 instance attributes:
    skills (an empty dictionary that will contain the skills of each player and its mana cost)
    and a guild set to "Unaffiliated" by default.

The Player class should also have two additional methods:

-	add_skill(skill_name, mana_cost)
    o	Adds the skill and the corresponding mana cost to the dictionary of skills.
        Returns "Skill {skill_name} added to the collection of the player {player_name}"
    o	If the skill is already in the collection, return "Skill already added"

-	player_info()
    o	Returns the player's information, including their skills, in this format:
        "Name: {player_name}
        Guild: {guild_name}
        HP: {hp}
        MP: {mp}
        ==={skill_name_1} - {skill_mana_cost}
        ==={skill_name_2} - {skill_mana_cost}
 …
        ==={skill_name_N} - {skill_mana_cost}"

The Guild class receives a name (string).
The Guild should also have one instance attribute players (an empty list which will contain the players of the guild).

The class also has 3 additional methods:
-	assign_player(player: Player)
    o	Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
    o	If he is already in the guild, returns
            "Player {player_name} is already in the guild."
    o	If the player is in another guild, returns "Player {player_name} is in another guild."


-	kick_player(player_name: str)
    o	Removes the player from the guild and returns "Player {player_name} has been removed from the guild.".
        Remember to change the player's guild in the player class to "Unaffiliated".
    o	If there is no such player in the guild, returns "Player {player_name} is not in the guild."

-	guild_info()
o	Returns the guild's information, including the players in the guild, in the format:
    "Guild: {guild_name}
{first_player's info}
…
{Nplayer's info}"


"""


##########: SOLUTION :##########

from project.player import Player
from project.guild import Guild

##########: TEST CODE :##########
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())


"""
Outout:

Skill Shield Break added to the collection of the player George
Name: George
Guild: Unaffiliated
HP: 50
MP: 100
===Shield Break - 20

Welcome player George to the guild UGT
Guild: UGT
Name: George
Guild: UGT
HP: 50
MP: 100
===Shield Break - 20

"""


##########: UNITTEST :##########

import unittest


class PlayerTest(unittest.TestCase):

    def test_player_init(self):
        player = Player("Pesho", 90, 90)
        result = player.player_info().strip()
        expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90"
        self.assertEqual(result, expected)

    def test_adding_skill_should_work(self):
        player = Player("Pesho", 90, 90)
        message = player.add_skill("A", 3)
        expected = "Skill A added to the collection of the player Pesho"
        self.assertEqual(message, expected)

    def test_adding_existing_skill_should_not_work(self):
        player = Player("Pesho", 90, 90)
        player.add_skill("A", 3)
        message = player.add_skill("A", 3)
        expected = "Skill already added"
        self.assertEqual(message, expected)

    def test_info(self):
        player = Player("Pesho", 90, 90)
        player.add_skill("A", 3)
        message = player.player_info().strip()
        expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3"
        self.assertEqual(message, expected)

    def test_guild_init(self):
        guild = Guild("GGXrd")
        message = guild.guild_info().strip()
        expeted = "Guild: GGXrd"
        self.assertEqual(message, expeted)

    def test_assign_working(self):
        guild = Guild("GGXrd")
        player = Player("Pesho", 90, 90)
        message = guild.assign_player(player)
        expected = "Welcome player Pesho to the guild GGXrd"
        self.assertEqual(message, expected)

    def test_assigning_player_in_the_same_guild(self):
        guild = Guild("GGXrd")
        player = Player("Pesho", 90, 90)
        guild.assign_player(player)
        message = guild.assign_player(player)
        expected = "Player Pesho is already in the guild."
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()
