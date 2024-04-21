""" """
from collections import deque

prepared_food = int(input())

order_queue = deque(int(x) for x in input().split())
print(max(order_queue))

# orders = list(map(int, input().split()))
# max_order = max(orders)
# print(max_order)
#
# order_queue = deque(orders)


while order_queue:
    next_order = order_queue.popleft()
    if next_order <= prepared_food:
        prepared_food -= next_order
    else:
        order_queue.appendleft(next_order)
        break

if not order_queue:
    print("Orders complete")
else:
    print("Orders left:", " ".join(map(str, order_queue)))


""" CEO """

# from collections import deque
#
# quantity_of_the_food = int(input())
# orders = deque(int(x) for x in input().split())
# print(max(orders))
#
# while orders:
#     order_number = orders.popleft()
#     if quantity_of_the_food - order_number >= 0:
#         quantity_of_the_food -= order_number
#     else:
#         print(f"Orders left: {order_number}", *orders)
#         break
# else:
#     print("Orders complete")


