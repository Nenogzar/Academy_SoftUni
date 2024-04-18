parentheses = input()
push = []
for index in range(len(parentheses)):
    if parentheses[index] == '(':
        push.append(index)
    elif parentheses[index] == ')':
        start_index = push.pop()
        end_index = index+1
        print(parentheses[start_index:end_index])


# input:
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# output:
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))

# input:
# (2 + 3) - (2 + 3)
# output:
# (2 + 3)
# (2 + 3)