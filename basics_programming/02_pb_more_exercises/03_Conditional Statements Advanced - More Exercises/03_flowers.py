number_chrysanthem = int(input())  # броят на закупените хризантеми – цяло число в интервала [0 ... 200]
number_rosses = int(input())  # броят на закупените рози – цяло число в интервала [0 ... 200]
number_tulips = int(input())  # броят на закупените лалета – цяло число в интервала [0 ... 200]
season = input()  # сезон– [Spring, Summer, Autumn, Winter]
type_days = input().upper()  # дали денят е празник – [Y – да / N - не]

price_chrysanthem = 0
price_rosses = 0
price_tulips = 0
number_flowers = number_chrysanthem + number_rosses + number_tulips
price_to_arrange = 2        # цена за аранжиране

if season == "Spring" or season == "Summer":
    price_chrysanthem = 2
    price_rosses = 4.10
    price_tulips = 2.5
elif season == "Autumn" or season == "Winter":
    price_chrysanthem = 3.75
    price_rosses = 4.5
    price_tulips = 4.15
else:
    print('error')

if type_days == "Y":
    price_chrysanthem *= 1.15
    price_rosses *= 1.15
    price_tulips *= 1.15

price_bouquet = number_rosses * price_rosses + number_chrysanthem * price_chrysanthem + number_tulips * price_tulips

# print(f"price_bouquet: {price_bouquet}")

if season == "Spring" and number_tulips > 7:
    price_bouquet *= 0.95

if season == "Winter" and number_rosses >= 10:
    price_bouquet *= 0.9

if number_flowers > 20:
    price_bouquet *= 0.8

price_bouquet += price_to_arrange

print(f"{price_bouquet:.2f}")



#
#
# chrysanthemums_buy = int(input())
# roses_buy = int(input())
# tulips_buy = int(input())
# season = input()
# is_it_holiday = input()
#
# flower_shop_info = {
#     "Spring": {
#         "chrysanthemums": 2.00,
#         "tulips": 2.50,
#         "roses": 4.10},
#     "Summer": {
#         "chrysanthemums": 2.00,
#         "tulips": 2.50,
#         "roses": 4.10},
#     "Autumn": {
#         "chrysanthemums": 3.75,
#         "tulips": 4.15,
#         "roses": 4.50},
#     "Winter": {
#         "chrysanthemums": 3.75,
#         "tulips": 4.15,
#         "roses": 4.50},
#     "Off": {
#         "7 > tulips spring": 0.05,
#         "10 > roses winter": 0.10,
#         "20 > all seasons": 0.20}
# }
# holiday_prices = 0.15
# total_flowers_buy = chrysanthemums_buy + roses_buy + tulips_buy
# creating_bucket = 2
# chrysanthemums_prices = chrysanthemums_buy * flower_shop_info[season]["chrysanthemums"]
# roses_prices = roses_buy * flower_shop_info[season]["roses"]
# tulips_prices = tulips_buy * flower_shop_info[season]["tulips"]
# total = (chrysanthemums_prices + roses_prices + tulips_prices)
#
# if is_it_holiday == "Y":
#     holiday_added = (chrysanthemums_prices + roses_prices + tulips_prices) * holiday_prices
#     total +=  + holiday_added
#     if tulips_buy > 7 and season == "Spring":
#         total += - (total * flower_shop_info["Off"]["7 > tulips spring"])
#     if roses_buy >= 10 and season == "Winter":
#         total += - (total * flower_shop_info["Off"]["10 > roses winter"])
#     if total_flowers_buy > 20:
#         total += - (total * flower_shop_info["Off"]["20 > all seasons"])
# else:
#     if tulips_buy > 7 and season == "Spring":
#         total += - (total * flower_shop_info["Off"]["7 > tulips spring"])
#     if roses_buy >= 10 and season == "Winter":
#         total += - (total * flower_shop_info["Off"]["10 > roses winter"])
#     if total_flowers_buy > 20:
#         total += - (total * flower_shop_info["Off"]["20 > all seasons"])
#
# total += + creating_bucket
# print(f"{total:.2f}")