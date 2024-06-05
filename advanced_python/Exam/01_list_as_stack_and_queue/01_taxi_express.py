# ******* Retake Exam - 19 August 2020 ******* #

# *******  01_taxi_express  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2463#0

You have created your own taxi company called "Taxi Express".
You want to analyze how well your taxi drivers are doing by calculating how much time they need to tend the customers.

You will receive a list of the cutomers (numbers seperated by comma and space ", ")
    on the first line and list of your taxis (numbers seperated by comma and space ", ").

Each number from the customer list represents how much time it takes to drive the customer to his/her destination.
Each number from the taxis list represents how much time they can drive, before they need to refill their tanks.
Keep track of the total time passed to drive all the customers to their destinations (values of all customers).

Each time you tend customers you should put the first customer in the last taxi until there are no customers left.
•	If the taxi can drive the customer to his/her destination,
    he does and you must add the time passed to drive the customer to his/her destination
    (the value of the current customer) to the total time. Remove both the customer and the taxi.

•	If the taxi cannot drive the customer to his/her destination,
    leave the customer at the beginning of the queue and remove the taxi.

At the end if you have successfully driven all the customers to their destinations, print

"All customers were driven to their destinations"
"Total time: {total_time} minutes"
Otherwise, if you ran out of taxis and there are still some customers left print
"Not all customers were driven to their destinations"
"Customers left: {left_customers joined by ", "}"


Input
•	On the first line you are given the customers – numbers seperated by comma and space ", "
•	On the second line you are given the taxis – numbers seperated by comma and space ", "
Output
•	Print the output as described above
Constraints
•	You will always have at least one customer and at least one taxi
Examples

Input
4, 6, 8, 5, 1
1, 9, 15, 10, 6

Output
All customers were driven to their destinations
Total time: 24 minutes


Input
10, 5, 8, 9
2, 4, 5, 8

Output
Not all customers were driven to their destinations
Customers left: 10, 5, 8, 9


Input
2, 8, 4, 3, 11, 7
10, 15, 4, 6, 3, 10, 2, 1


Output
All customers were driven to their destinations
Total time: 35 minutes

"""

##########: variant 1 :##########
from collections import deque

customers = deque(map(int, input().split(", ")))
taxis = deque(map(int, input().split(", ")))
total_time = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()

    if customer <= taxi:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str, customers))}")

##########: variant 2 :##########

from collections import deque
customers = deque(int(x) for x in input().split(", "))
taxi_drivers = deque(int(x) for x in input().split(", "))
total_minutes = 0
while customers and taxi_drivers:
    current_taxi = taxi_drivers.pop()
    if customers[0] <= current_taxi:
        total_minutes += customers.popleft()
if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_minutes} minutes")
elif customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")


##########: variant 3 solution SoftUni :##########


