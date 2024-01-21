import math

while True:

    year_type = input("каква е годината: leap or normal : ")
    p = int(input("Броя на празниците в годината: "))
    h = int(input("Броя на почивните дни в които е на село: "))
    weekend = 48

    weekend_in_sofia = (weekend - h) * 0.75 # Играе в София 3/4 от уикендите
    #print(f"weekend_in_sofia{math.floor(weekend_in_sofia)}")

    holidays_in_sofia = p * 0.6666667 # играе в София 2/3 от празниците
    #print(f"holidays_in_sofia {math.floor(f"{leap_yaer:.0f}")}")

    all_play_days = weekend_in_sofia + holidays_in_sofia + h #
    #print(f"all_play_days{math.floor(all_play_days)}")

    if year_type == "leap":
        leap_yaer = all_play_days * 1.15
        #print(f" year leap{math.floor(all_play_days)}")
        print(math.floor((leap_yaer)))
    elif year_type == "normal":
        print(math.floor(all_play_days))
    else:
        print("неправилен вид на година")



    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
