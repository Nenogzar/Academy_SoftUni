# z = [1,2,3]
# for x in z:
#     print(x)
############

# Списък от числа:
nums=[5,10,1,60,25,3]

# Първи елемент:
print("Първи елемент:",nums[0])

# Second element
print("Втори елемент:",nums[1])

# Промяна на стойността на елемент в списъка:
nums[1]="текст"

# Дължина на list
great = 'Hello Bob'
print("Дължината на стринг Hello Bob е -> ", len(great))
# Дължина на списъка:
print("Дължина на списъка nums:", len(nums))

# range and len

friends = ['Josef', 'Glean', 'Sally']

print('len friend', len(friends))
print(type(len(friends)))
# output
# len friend 3
# <class 'int'>

print('range len friend', range(len(friends)))
print(type(range(len(friends))))
# output
# range len friend range(0, 3)
# <class 'range'>

for friend1 in friends:
    print('Happy New Year ', friend1)
# output
# Happy New Year  Josef
# Happy New Year  Glean
# Happy New Year  Sally

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year ', friend)
# output
# Happy New Year  Josef
# Happy New Year  Glean
# Happy New Year  Sally

