country_names = input().split(", ")
capytal_name = input().split(", ")
country_dict = dict(zip(country_names, capytal_name))

[print(f"{country} -> {capital}") for country, capital in country_dict.items()]

