#1
number = int(input())
counter = 1
all_is_printed = False
for row in range(1, number +1):
    for column in range(1, row +1):
        print(counter, end = " ")
        counter += 1
        if counter > number:
            all_is_printed = True
            break
    if all_is_printed: # if all_is_printed == True
        break
    print()


#2

first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    even_digits_sum = 0
    odd_digits_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(current_number_as_string, end=" ")


#3
prime_numbers_sum = 0
non_prime_numbers_sum = 0
command = input()
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        current_number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:  # current_number is not prime
                current_number_is_prime = False
                break
        if current_number_is_prime:  # if current_number_is_prime == True
            prime_numbers_sum += current_number
        else:
            non_prime_numbers_sum += current_number
    command = input()
print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")


#4

number_of_jury = int(input())
final_grade = 0
number_of_presentations = 0
command = input()
while command != "Finish":
    current_presentation_name = command
    current_presentation_grades = 0
    number_of_presentations += 1
    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        current_presentation_grades += current_grade
    current_presentation_average_grade = current_presentation_grades / number_of_jury
    print(f"{current_presentation_name} - {current_presentation_average_grade:.2f}.")
    final_grade += current_presentation_average_grade
    command = input()
final_average_grade = final_grade / number_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}." )

#5

number = int(input())
for current_number in range(1111, 9999 + 1):
    current_number_as_string = str(current_number)
    current_number_is_special = True
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            current_number_is_special = False
            break
    if current_number_is_special:  # if current_number_is_special == True
        print(current_number, end=" ")


#6


student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    sold_tickets = 0
    for ticket in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_tickets += 1
        elif current_ticket == "standard":
            standard_tickets += 1
        elif current_ticket == "kid":  # else
            kid_tickets += 1
        sold_tickets += 1
    percent_full_hall = sold_tickets / free_seats * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    movie_name = input()
total_tickets_sold = student_tickets + standard_tickets + kid_tickets
percent_student_tickets = student_tickets / total_tickets_sold * 100
percent_standard_tickets = standard_tickets / total_tickets_sold * 100
percent_kid_tickets = kid_tickets / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")

