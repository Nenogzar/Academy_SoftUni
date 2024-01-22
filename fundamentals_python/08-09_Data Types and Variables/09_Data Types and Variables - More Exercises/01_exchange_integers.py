""" 1 """

number_one = int(input())
number_two = int(input())

print(f"Before:\na = {number_one}\nb = {number_two}")
print(f"After:\na = {number_two}\nb = {number_one}")

""" 2 """

number_one = int(input())
number_two = int(input())

print(f"Before:\na = {number_one}\nb = {number_two}")

number_one, number_two = number_two, number_one

print(f"After:\na = {number_one}\nb = {number_two}")


