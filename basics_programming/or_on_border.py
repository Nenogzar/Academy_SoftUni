while True:
    x = int(input("x"))
    y = int(input("y"))
    x1 = int(input("x1"))
    y1 = int(input("y1"))
    x2 = int(input("x2"))
    y2 = int(input("y2"))

    on_left_site = (x == x1 and y >= y1 and y<= y2)
    on_right_site = (x == x2 and y >= y1 and y<= y2)
    on_up_site = (y == y1 and x >= x1 and x <= x2)
    on_down_site = (y == y2 and x >= x1 and x <= x2)

    if on_left_site or on_right_site or on_up_site or on_down_site:
        print("Border")
    else:
        print("Outsite/Insite")
    repeat = input("Y/N")
    if repeat.upper() == "N":
        print("10x")
        break