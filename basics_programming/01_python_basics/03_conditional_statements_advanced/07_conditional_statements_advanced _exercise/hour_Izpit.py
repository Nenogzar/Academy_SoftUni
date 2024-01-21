while True:
    hour_of_examine = int(input("час 0-23"))
    minutes_of_examine = int(input("минути 0 -59"))
    hour_of_arriving = int(input("час 0-23"))
    minutes_of_arriving = int(input("минути 0 -59"))

    time_of_examine = hour_of_examine * 60 + minutes_of_examine #времето на изпита
    time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving

    if time_of_arriving > time_of_examine:
        print("Late")
    elif time_of_examine-30 <= time_of_arriving <= time_of_examine:
        print("On time")
    else:
        print("Early")

    if time_of_examine-60 < time_of_arriving < time_of_examine:
        print(f"{time_of_examine-time_of_arriving:0>2d} minutes before the start")
    elif time_of_arriving <= time_of_examine - 60:
        difference = time_of_examine - time_of_arriving
        hour =difference // 60
        minets =difference % 60
        print(f"{hour}:{minets:0>2d} hours before the start")
    elif time_of_examine < time_of_arriving < time_of_examine+60:
        print(f"{time_of_arriving-time_of_examine} minutes after the start")
    elif time_of_arriving >= time_of_examine+60:
        difference=time_of_arriving - time_of_examine
        hour=difference // 60
        minets=difference % 60
        print(f"{hour:0>2d}:{minets:0>2d} hours after the start" )

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
