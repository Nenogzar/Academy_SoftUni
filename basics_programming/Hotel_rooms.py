months = input("May, June, July, August, September, October: ")
night = int(input("Брой на нощувки"))
studio_price = 0.00
apartment_price = 0.00
apartment_rent = 0.00
studio_rent = 0.00

if months == "May" or months=="October":
    studio_price = 50.00
    apartment_price = 65.00

    apartment_rent = apartment_price * night
    studio_rent = studio_price * night
    if night > 14:
        studio_rent *= 0.70
        apartment_rent *= 0.90
    elif night > 14:
        studio_rent *= 0.95

elif months == "June" or months == "September":
    apartment_price =68.70
    studio_price =75.20

    apartment_rent = night  * apartment_price
    studio_rent = night * studio_price

    if night > 14:
        apartment_rent *= 0.90
        studio_rent *= 0.80
elif months == "July" or months == "August":
    apartment_price = 77
    studio_price = 76

    apartment_rent = apartment_price * night
    if night > 14:
        apartment_rent *= 0.90
    studio_rent= studio_price * night

else:
    print ("Wrong monts")

print(f"Apartment: {apartment_rent:.2f}lv.")
print(f"Studio: {studio_rent:.2f}lv.")