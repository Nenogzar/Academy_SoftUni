country = input().split(", ")
capital = input().split(", ")


country_cap_dict = dict(zip(country,capital))

for key, value in country_cap_dict:
    print(key, value)

