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


""" qceka88  """
from collections import deque


class HotPotato:

    def __init__(self):
        self.kids = deque(input().split())
        self.rotations = int(input())
        self.message = []
        self.rotate_kids()

    def return_message(self):
        print('\n'.join(f'Removed {name}' for name in self.message[:-1]))
        print(f'Last is {self.message[-1]}')

    def rotate_kids(self):
        while self.kids:
            self.kids.rotate(-self.rotations)
            self.message.append(self.kids.pop())
        self.return_message()


if __name__ == '__main__':
    HotPotato()


