players = {}

while True:
    name = input()
    if name == "END":
        break

    goals = int(input())

    if name not in players:
        players[name] = goals
    else:
        players[name] += goals

    best_player = max(players, key=players.get)

    if players[name] >= 10:
        break
# print(f"{players}")
print(f"{best_player} is the best player!")

if players[best_player] >= 3:
    print(f"He has scored {players[best_player]} goals and made a hat-trick !!!")
else:
    print(f"He has scored {players[best_player]} goals.")

