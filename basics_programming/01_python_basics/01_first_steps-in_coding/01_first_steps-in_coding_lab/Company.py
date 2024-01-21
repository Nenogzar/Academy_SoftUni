camp_day=int(input("Колко дни ще се провежда кампанията? "))
camp_shefs=int(input("Колко сладкаря ще участват? "))
camp_cake=int(input("Колко торти ще са нужни? "))
cam_gofret=int(input("Колко гофрети ще са нужни? "))
cam_palach=int(input("Колко палаченики ще са нужни? "))
price_cake=45*camp_cake
print(price_cake)
price_gofret=5.80*cam_gofret
print(price_gofret)
price_palach=3.20*cam_palach
print(price_palach)
price_total_day= (price_palach+price_gofret+price_cake)*camp_shefs
print(price_total_day)
price_total=price_total_day*camp_day
print(price_total)
price=price_total-price_total/8
print(f"{price:.2f}")

