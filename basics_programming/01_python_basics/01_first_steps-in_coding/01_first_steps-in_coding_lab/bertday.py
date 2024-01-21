rent_price = int(input("коко е наема на залата? "))
rent_cake = (rent_price * 20)/100
rent_shweps = rent_cake - (rent_cake*45)/100
rent_charli = rent_price / 3
price_total = rent_price+rent_charli+rent_cake+rent_shweps
print(f"при наем на зала {rent_price}лв. тортата ще струва {rent_cake}лв., напитките ще струват {rent_shweps}лв. Ще са Ви нужни {price_total:.2f}лв. за празненството.")