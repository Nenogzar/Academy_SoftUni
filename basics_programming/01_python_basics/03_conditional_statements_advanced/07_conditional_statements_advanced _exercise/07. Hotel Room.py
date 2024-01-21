months = input().lower()
nights = int(input())

studio_price = 0
apartment_price = 0
studio_rent = 0.00
apartment_rent = 0.00

if months == "may" or months == "october":
    studio_price = 50
    apartment_price = 65
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        studio_rent *= 0.7
        apartment_rent *= 0.9
    elif 7 < nights < 14:
        studio_rent *= 0.95
elif months == "june" or months == "september":
    studio_price = 75.20
    apartment_price = 68.70
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        studio_rent *= 0.80
        apartment_rent *= 0.90
elif months == "july" or months == "august":
    studio_price = 76
    apartment_price = 77
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        apartment_rent *= 0.90
else:
    print("error")

#if nights > 14:
#    apartment_rent *= 0.90

studio_info = f"Studio: {studio_rent:.2f} lv."
apartment_info = f"Apartment: {apartment_rent:.2f} lv."

print(apartment_info)
print(studio_info)
