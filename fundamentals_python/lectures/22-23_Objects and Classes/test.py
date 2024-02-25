def numbers(num=1):
    num += 1
    return num


print(numbers())
print(numbers())
print(numbers())
print(numbers())
print("_____________")


# Това е проблемното
def numbers1(numb=[0, 1, 2]):
    for k in range(len(numb)):
        numb[k] += 1
    return numb


print(numbers1())
print(numbers1())
print(numbers1())
print(numbers1())
print("_____________")


def numbers2(numb=[0, 1, 2]):
    numb = [x + 1 for x in numb]
    return numb


print(numbers2())
print(numbers2())
print(numbers2())
print(numbers2())
print("_____________")
