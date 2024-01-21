while True:

    budget=float(input("С какъв бюджет разполагам: "))
    seson =input("през кой сезон ще почивам? summer or winter ")
    destination = ""
    dest_type = ""


    if budget <=0:
        print("Нямате пари за цигари камоли за почивка")
        continue
    elif budget <= 100:
        destination = "Bulgaria"
        if seson == "summer":
            budget=budget * 0.3
        elif seson == "winter":
            budget=budget * 0.7
    elif budget <= 1000:
        destination = "Balkans"
        if seson == "summer":
            budget=budget * 0.4
        elif seson == "winter":
            budget=budget * 0.8
    else:
        destination = "Europe"
        budget=budget* 0.9

    #print((budget))
    if 0 < budget <= 50:
        dest_type = "Camp"
    elif budget > 50:
        dest_type = "Hotel"
    else:
        print("Ще сис стоя във вкъщи!")

    print(f"Somewhere in {destination} {dest_type}  - {budget:.2f}lv.")

    #повторение на програмата
    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
