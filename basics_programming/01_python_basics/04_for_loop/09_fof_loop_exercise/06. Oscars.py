actor_name = input()
points_academy = float(input())
number_jury = int(input())
point_jury = 0

for point in range(number_jury):
    jury_name = input()
    points = float(input())
    lend_jury_name = len(jury_name)
    points_academy += ((lend_jury_name * points)/2)
    print(f"{lend_jury_name}*{points}/2+{points_academy} = {points_academy}")
    if points_academy >= 1250.50:
        break
need_points = abs(1250.50 - points_academy)

if points_academy >= 1250.50:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_academy:.1f}!")
elif points_academy < 1250.50:
    print(f"Sorry, {actor_name} you need {need_points:.1f} more!")

