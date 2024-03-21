# import re
# def valid_distans(pattern_data):
#     travel_points =0
#     pattern = r"(\=|\/)([A-Za-z]{2,})\1"
#     valid_distansion = []
#     result = re.finditer(pattern, pattern_data)
#
#     for destination in result:
#         key, valid_d = destination.group(1), destination.group(2)
#         valid_distansion.append(valid_d)
#         travel_points += len(valid_d)
#
#     print(f"Destinations: {', '.join(valid_distansion)}\nTravel Points: {travel_points}")
#
# data = input()
# total = valid_distans(data)


import re

def valid_distans(pattern_data):
    travel_points = 0
    pattern = r"(\=|\/)([A-Z][a-zA-Z]{2,})\1"
    valid_destinations = re.findall(pattern, pattern_data)

    destinations = [match[1] for match in valid_destinations]
    travel_points = sum(len(destination) for destination in destinations)

    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_points}")

input_string = input()

valid_distans(input_string)
