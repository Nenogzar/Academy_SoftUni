water = 0
internet = 0
month = int(input())
electricity_mont = 0
other_element = 0
other = 0
total_sum = 0
for mon in range(month):
    electricity = float(input())
    electricity_mont += electricity
    water += 20
    internet += 15
    other_element = water + internet + electricity_mont  # Calculate totals for the current month
    other = other_element + (other_element * 0.2)  # Calculate the other expenses for the current month
    total_sum = other_element + other
print(f"Electricity: {electricity_mont:.2f} lv")         # Electricity (total for all months)
print(f"Water: {water:.2f} lv")                    # Water (total for all months)
print(f"Internet: {internet:.2f} lv")                 # Internet (total for all months)
print(f"Other: {other:.2f} lv")                    # Other (total for the last month)
print(f"Average: {(total_sum / month):.2f} lv")    # Average (average for all months)



# months = int(input())
#
# electricity_bill = 0
# water_bill = 20
# internet = 15
# others = 0
# bills_count = 0
#
# for _ in range(1, months + 1):
#     electricity_bill_mount = float(input())
#     electricity_bill += electricity_bill_mount
#     others += (electricity_bill_mount + water_bill + internet) + (electricity_bill_mount + water_bill + internet) * 0.20
#     bills_count += 1
#
# internet = internet * months
# water_bill = water_bill * months
# average_bill = (electricity_bill + water_bill + internet + others) / months
#
# print(f"Electricity: {electricity_bill:.2f} lv")
# print(f"Water: {water_bill:.2f} lv")
# print(f"Internet: {internet:.2f} lv")
# print(f"Other: {others:.2f} lv")
# print(f"Average: {average_bill:.2f} lv")
