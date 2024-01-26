# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# Print the resulting integer list.

number_list, zero_list, event_list = [], [], input()

for num in event_list.split(", "):
    number = int(num)
    if number == 0:
        zero_list.append(number)
    else:
        number_list.append(number)
output_list =number_list + zero_list
print(output_list)

############## FROM CEO ##########################

# numbers = list(map(int, input().strip().split(", ")))
#
# for _ in numbers:
#     numbers.append(numbers.pop(numbers.index(0)))
# print(numbers)
