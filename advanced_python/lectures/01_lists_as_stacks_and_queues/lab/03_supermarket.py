from collections import deque

people = input()
customers = deque()
while people != "End":
    if people == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(people)

    people = input()
print(f"{len(customers)} people remaining.")
