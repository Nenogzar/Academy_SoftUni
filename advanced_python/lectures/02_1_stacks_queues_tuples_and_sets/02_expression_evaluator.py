from collections import deque

string_expression = input().split()

numbers = deque()
operators = {
    "+": lambda f, s: f + s,
    "-": lambda f, s: f - s,
    "*": lambda f, s: f * s,
    "/": lambda f, s: f // s
}


for element in string_expression:
    if element in "+-*/":
        while len(numbers) > 1:
            numbers.appendleft(operators[element](numbers.popleft(), numbers.popleft()))
    else:
        numbers.append(int(element))

print(numbers.popleft())