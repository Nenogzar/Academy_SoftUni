import time
start_time = time.time()
"""test value """
# input:
# Tracy Emily Daniel
# 2
#
# output:
# Removed Emily
# Removed Tracy
# Last is Daniel

"""whit deque rotate """
# from collections import deque
# kids = deque(input().split())
# skips = int(input())
# while len(kids) > 1:
#     kids.rotate(-skips)
#     print(f"Removed {kids.pop()}")
# print(f"Last is {''.join(kids)}") # ex time = 1.45


"""   """
from collections import deque
kids = deque(input().split())
tosses = int(input())

while len(kids) > 1:
    for num in range(1, tosses + 1):
        if num % tosses == 0:
            print(f"Removed {kids.popleft()}")
            break
        kids.append(kids.popleft())

print(f"Last is {kids.pop()}")  #ex time = 1.38


end_time = time.time()
execution_time = (end_time - start_time)
print(f"Execution time: {execution_time:.2f} seconds")
