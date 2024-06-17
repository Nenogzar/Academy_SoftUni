A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([x for y in A for x in y])


for i in A:
    print(*i, end=" ")
print()

for n in A:
    for m in n:
        print(m, n)



a = [1,2,3]
b = [4,5]
b.append(a)

print(b)
