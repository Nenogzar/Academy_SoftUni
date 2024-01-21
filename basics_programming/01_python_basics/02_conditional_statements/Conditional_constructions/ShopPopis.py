while True:

    exkurzia = float(input("Цената на екскурзията е: "))
    paz = int(input("Брой на пъзелите: "))
    kukli = int(input("Брой на кукли: "))
    bears = int(input("Брой на мечета: "))
    minyons = int(input("Брой на миньони: "))
    trax = int(input("Брой на камиончета: "))

    porachka = paz + kukli + bears + minyons + trax
    #print(f" Брой на играчките {porachka}")

    pricepaz = paz * 2.60
    #print(pricepaz)
    pricekukli = kukli * 3
    #print(pricekukli)
    pricebears = bears * 4.1
    #print(pricebears)
    pricemin = minyons * 8.2
    #print(pricemin )
    pricetrak = trax * 2
    #print(pricetrak)


    ordervalue = pricemin + pricetrak + pricebears + pricekukli + pricepaz
    #print(f" целата сума {ordervalue}")


    if porachka >= 50:
        ordervalue = ordervalue - ordervalue * 0.25

    pechmaga = ordervalue * 0.1
    #print(ordervalue)
    #print(pechmaga)
    pechalba = ordervalue - pechmaga
    #print(pechalba)
    if pechalba >= exkurzia:
        print(f"Yes! {pechalba - exkurzia:.2f} lv left.")
    else:
        print(f"Not enough money! {pechalba - exkurzia:.2f} lv needed.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break