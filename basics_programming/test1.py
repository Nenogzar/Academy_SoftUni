days_tour = int(input())
win_game = 0
lost_game = 0
win_days = 0
lost_days = 0
total_points = 0

for day in range(1, days_tour + 1):
    game = input()
    if game == "Finish":
        break

    result = input()

    if result == "win":
        win_game += 20
        win_days += 1
    elif result == "lose":
        lost_game += 10
        lost_days += 1

    total_points += win_game

if win_days > lost_days:
    total_points *= 1.2

if win_game > lost_game:
    total_points *= 1.1

if win_days > days_tour - win_days:
    print(f"You won the tournament! Total raised money: {total_points * 1.2:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_points:.2f}")
