# 3.	Football Cards
# Most football fans love it for the goals and excitement.
# Well, this problem does not. You are up to handle the referee's little notebook
# and count the players who were sent off for fouls and misbehavior.
# The rules:
# Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card.
# If one of the teams has less than 7 players remaining, the referee stops the game immediately,
# and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. e.g.,
# the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space.
# You should print the count of remaining players on each team at the end of the game in the format:
# "Team A - {players_count}; Team B - {players_count}".
# If the referee terminated the game, print an additional line: "Game was terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.

letters = "AB"
numbers = list(range(1, 12))
combined_list = [f"{letter}-{num}" for letter in letters for num in numbers]
remaining_a = 11
remaining_b = 11

user_input = input().split()

for item in user_input:
    if item in combined_list:
        combined_list.remove(item)
        if item.startswith("A"):
            remaining_a -= 1
        else:
            remaining_b -= 1
    if remaining_a <= 6 or remaining_b <= 6:
        print(f"Team A - {remaining_a}; Team B - {remaining_b}")
        print("Game was terminated")
        break

else:
    print(f"Team A - {remaining_a}; Team B - {remaining_b}")

################################################################################
#
# team_a_players = set(range(1, 11+1))
# team_b_players = set(range(1, 11+1))
# cards = input().split()
#
# for card in cards:
#     team, player = card.split('-')
#     player = int(player)
#
#     if team == 'A' and player in team_a_players:
#         team_a_players.remove(player)
#     elif team == 'B' and player in team_b_players:
#         team_b_players.remove(player)
#     remaining_team_a = len(team_a_players)
#     remaining_team_b = len(team_b_players)
#
#     if len(team_a_players) < 7 or len(team_b_players) < 7:
#         print(f"Team A - {remaining_team_a}; Team B - {remaining_team_b}")
#         print("Game was terminated")
#         break
#
# else:
#     print(f"Team A - {remaining_team_a}; Team B - {remaining_team_b}")


########################### FROM CIO ############################################

# cards_list = input().split(" ")
# game_terminated = False
# team_a = []
# team_b = []
#
# for card in cards_list:
#     if "A" in card and card not in team_a:
#         team_a.append(card)
#     elif "B" in card and card not in team_b:
#         team_b.append(card)
#     if len(team_a) > 4 or len(team_b) > 4:
#         game_terminated = True
#         break
#
# print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}")
# if game_terminated:
#     print("Game was terminated")


########################################################################################################################

# team_information = input().split(" ")
# terminated = False
# teams_info = []
# for team_num in range(1, 12):
#     teams_info.append(f"A-{team_num}")
#     teams_info.append(f"B-{team_num}")
#
# for player in team_information:
#     if player in teams_info:
#         teams_info.remove(player)
#         if any([sum([x.count("A") for x in teams_info]) < 7, sum([x.count("B") for x in teams_info]) < 7]):
#             terminated = True
#             break
#
# print(f"Team A - {sum([x.count('A') for x in teams_info])}; Team B - {sum([x.count('B') for x in teams_info])}")
# if terminated:
#     print("Game was terminated")


########################################################################################################################

#
#
# team_information = input().split()
# terminated = False
# team_a = set()
# team_b = set()
# for team_num in range(1, 12):
#     team_a.add(f"A-{team_num}")
#     team_b.add(f"B-{team_num}")
#
# for player in range(1, len(team_information) + 1):
#     if team_information[player - 1] in team_a:
#         if len(team_a.difference(set(team_information[:player]))) < 7:
#             terminated = True
#             break
#     elif team_information[player - 1] in team_b:
#         if len(team_b.difference(set(team_information[:player]))) < 7:
#             terminated = True
#             break
#
#
# print(f"Team A - {len(team_a.difference(set(team_information[:player])))}; Team B - {len(team_b.difference(set(team_information[:player])))}")
# if terminated:
#     print("Game was terminated")
#
########################################################################################################################
#
# team_information = input()
#
# team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_list = team_information.split(" ")
#
# for letter in team_list:
#
#     if letter[0] == "A":
#         if int(letter[2:]) in team_a:
#             team_a.remove(int(letter[2:]))
#
#     elif letter[0] == "B":
#         if int(letter[2:]) in team_b:
#             team_b.remove(int(letter[2:]))
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {(len(team_b))}")
#
# if len(team_a) < 7 or len(team_b) < 7:
#     print("Game was terminated")