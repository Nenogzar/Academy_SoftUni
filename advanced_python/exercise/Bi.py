from collections import deque
import operator

some_string = deque(input().split())
sings = {"*": operator.mul,
         "+": operator.add,
         "-": operator.sub,
         "/": operator.floordiv}
result = deque()

for current_char in some_string:
    if current_char in sings.keys():
        while len(result) >= 2:
            first_number = result.popleft()
            second_number = result.popleft()
            current_result = sings[current_char](first_number, second_number)
            result.appendleft(current_result)
    else:
        result.append(int(current_char))

print(*result)

# input1: 6 3 - 2 1 * 5 /
# output: 1

# input2: 2 2 - 1 *
# output: 0

# input3: 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
# output: 164
