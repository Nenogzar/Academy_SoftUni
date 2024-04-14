parentheses = input()
push = []
for index in range(len(parentheses)):
    if parentheses[index] == '(':
        push.append(index)
    elif parentheses[index] == ')':
        start_index = push.pop()
        end_index = index+1
        print(parentheses[start_index:end_index])


