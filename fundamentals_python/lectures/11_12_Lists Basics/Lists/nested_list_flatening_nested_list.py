start = int(input("start range: "))
end = int(input("end range: "))
step = int(input("steps: "))
input_string = list(range(start, end+1, step))
result = list(map(list, zip(*[iter(input_string)]*2)))
if len(input_string) % 2 != 0:
    result.append([input_string[-1]])
print(result)
