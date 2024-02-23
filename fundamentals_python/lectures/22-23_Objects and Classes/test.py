def info(val = [1,2,3]):
    for num in range(len(val)):
        val[num] += 1
    return val

print(info())
print(info())
print(info())



def info1(val1 = 1):
    val1 += 1
    return val1

print(info1())
print(info1())
print(info1())