first_match = input() # формат "2:0", "0:1", "1:1" и т.н.
second_match = input()
third_match = input()

a1 = int(first_match[0])
a2 = int(first_match[-1])
b1 = int(second_match[0])
b2 = int(second_match[-1])
c1 = int(third_match[0])
c2 = int(third_match[-1])

win = 0
lost = 0
drawn = 0

if a1 > a2:
    win += 1
elif a1 < a2:
    lost += 1
elif a1 == a2:
    drawn += 1

if b1 > b2:
    win += 1
elif b1 < b2:
    lost += 1
elif b1 == b2:
    drawn += 1

if c1 > c2:
    win += 1
elif c1 < c2:
    lost += 1
elif c1 == c2:
    drawn += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")



# game_one_result = input()
# game_two_result = input()
# game_three_result = input()
#
#
# wins = 0
# loses = 0
# draws = 0
#
# if int(game_one_result[0]) > int(game_one_result[-1]):
#     wins += 1
# elif int(game_one_result[0]) < int(game_one_result[-1]):
#     loses += 1
# else:
#     draws += 1
#
# if int(game_two_result[0]) > int(game_two_result[-1]):
#     wins += 1
# elif int(game_two_result[0]) < int(game_two_result[-1]):
#     loses += 1
# else:
#     draws += 1
#
# if int(game_three_result[0]) > int(game_three_result[-1]):
#     wins += 1
# elif int(game_three_result[0]) < int(game_three_result[-1]):
#     loses += 1
# else:
#     draws += 1
#
# print(f"Team won {wins} games.")
# print(f"Team lost {loses} games.")
# print(f"Drawn games: {draws}")




# wins = 0
# loses = 0
# draws = 0
#
# for games in range(3):
#     game_result = input()
#     if int(game_result[0]) > int(game_result[-1]):
#         wins += 1
#     elif int(game_result[0]) < int(game_result[-1]):
#         loses += 1
#     else:
#         draws += 1
#
# print(f"Team won {wins} games.")
# print(f"Team lost {loses} games.")
# print(f"Drawn games: {draws}")
