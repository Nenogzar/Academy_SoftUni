# ******* Advanced Retake Exam - 14 April 2021 ******* #

# *******  01_pizza_orders  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2828#0

On the first line, you will receive a sequence of pizza orders.
    Each order contains a different number of pizzas, separated by comma and space ", ".
    On the second line, you will receive a sequence of employees with pizza-making capacities
        (how much pizzas an employee could make), separated by comma and space ", ".

Your task is to check if all pizza orders are completed.

To do that, you should take the first order and the last employee and see:

•	If the number of pizzas in the order is less than or equal to the employee's pizza making capacity,
        the order is completed. Remove both the order and the employee.
•	If the number of pizzas in the order is greater than the employee's pizza making capacity,
        the remaining pizzas from the order are going to be made by the next employees until the order is completed.
    o	If there are no more employees to finish the order, consider it not completed.

•	The restaurant does not take orders for more than 10 pizzas at once.
•	If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee.
You should keep track of the total pizzas that are being made.

Input
•	On the first line you will be given a sequence of pizza orders each represented as a number
        – integers separated by comma and space ", "
•	On the second line you will be given a sequence of employees with pizza-making capacities
        – integers separated by comma and space ", "

Output
•	If all orders are successfully completed, print:
All orders are successfully completed!
Total pizzas made: {total count}
Employees: {left employees joined by ", "}
•	Otherwise, if you ran out of employees and there are still some orders left print:
Not all orders are completed.
Orders left: {left orders joined by ", "}
Constraints
•	You will always have at least one order and at least one employee
•	All integers will be in range [-100, 100]

Examples
Input
11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1

Output
All orders are successfully completed!
Total pizzas made: 15
Employees: 3, 1


***** Comment *****
1) The restaurant do not take the first order for 11 pizzas.
2) The first employee (1) takes an order for 6 pizzas but could only make 1. 5 pizzas left.
3) The next employee (9) continues the same order for 5 pizzas. The order is completed. Remove both.
4) The next employee (5) takes an order for 8 pizzas but could only make 5. 3 pizzas left.
5) The next employee (10) continues the same order for 3 pizzas. The order is completed. Remove both.
6) The next employee (9) takes an order for 1 pizza. The order is completed. Remove both.
7) All orders are completed.

Input
10, 9, 8, 7, 5
5, 10, 9, 8, 7


Output
Not all orders are completed.
Orders left: 2, 5

***** Comment *****
1) The last employee (7) takes an order for 10 pizzas but could only make 7. 3 pizzas left.
2) The next employee (8) continues the same order for 3 pizzas. The order is completed. Remove both.
3) The next employee (9) takes an order for 9 pizzas. The order is completed. Remove both.
4) The next employee (10) takes an order for 8 pizzas. The order is completed. Remove both.
5) The next employee (5) takes an order for 7 pizzas but could only make 5. 2 pizzas left.
6) Orders are not completed.

Input
12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1


Output
All orders are successfully completed!
Total pizzas made: 5
Employees: 10, 15, 4, 6


"""

##########: variant 1 :##########

from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees = list(map(int, input().split(", ")))

pizza_counter = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()

    if order <= 0 or order > 10:
        continue

    employe = employees.pop()

    if employe >= order:
        pizza_counter += order
    else:
        pizza_counter += employe
        order -= employe
        pizza_orders.appendleft(order)

if not pizza_orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {pizza_counter}\nEmployees: {', '.join(map(str, employees))}")
else:
    print(f"Not all orders are completed.\nOrders left: {', '.join(map(str, pizza_orders))}")


##########: variant 2 :##########

from collections import deque


def get_input():
    pizza_orders = deque(map(int, input().split(", ")))
    employees = list(map(int, input().split(", ")))
    return pizza_orders, employees


def process_orders(pizza_orders, employees):
    pizza_counter = 0

    while pizza_orders and employees:
        order = pizza_orders.popleft()

        if order <= 0 or order > 10:
            continue

        employe = employees.pop()

        if employe >= order:
            pizza_counter += order
        else:
            pizza_counter += employe
            order -= employe
            pizza_orders.appendleft(order)

    return pizza_counter, pizza_orders, employees


def print_results(pizza_counter, pizza_orders, employees):
    if not pizza_orders:
        print(
            f"All orders are successfully completed!\nTotal pizzas made: {pizza_counter}\nEmployees: {', '.join(map(str, employees))}")
    else:
        print(f"Not all orders are completed.\nOrders left: {', '.join(map(str, pizza_orders))}")


def main():
    pizza_orders, employees = get_input()
    pizza_counter, pizza_orders, employees = process_orders(pizza_orders, employees)
    print_results(pizza_counter, pizza_orders, employees)


if __name__ == "__main__":
    main()

##########: variant 3 solution CEO :##########


from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
made_pizzas = 0

while pizza_orders and employees:
    pizza_order = pizza_orders.popleft()
    if pizza_order <= 0 or pizza_order > 10:
        continue
    employee = employees.pop()
    if pizza_order <= employee:
        made_pizzas += pizza_order
    elif pizza_order > employee:
        made_pizzas += employee
        pizza_orders.appendleft(pizza_order - employee)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {made_pizzas}")
    if employees:
        print(f"Employees: {', '.join(str(x) for x in employees)}")
elif not employees and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")


##########: variant 4 solution TANER :##########

from collections import deque
pizza_orders = deque(int(x) for x in input().split(", ") if 0 < int(x) <= 10)   #  COOOOOOL  :)
employees = deque(int(x) for x in input().split(", "))

total_pizzas = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    employee_capacity = employees.pop()

    if current_order > employee_capacity:
        current_order -= employee_capacity
        total_pizzas += employee_capacity
        pizza_orders.appendleft(current_order)
        continue

    total_pizzas += current_order
if not pizza_orders:
    print(f"""
    All orders are successfully completed!
    Total pizzas made: {total_pizzas}
    Employees: {', '.join(str(x) for x in employees)}
""")
elif pizza_orders:
    print(f"""
    Not all orders are completed.
    Orders left: {', '.join(str(x) for x in pizza_orders)}
""")

