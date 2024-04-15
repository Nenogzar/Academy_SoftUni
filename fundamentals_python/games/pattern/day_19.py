def pattren_x(num):
    for i in range(num):
        for j in range(num):
            for k in range(num):
                if i == k or i + k == (num - 1):
                    print('>>', end='')
                else:
                    print('  ', end='')
        print()
    # print('#' * 25)



num = int(input())
if num % 2 != 0:
    pattren_x(num)
else:
    num = num - 1
    pattren_x(num)



# l = [['']*num for _ in range(num)]
# n = -1
# for i, row in enumerate(l):
#     row[i], row[n] = '>','>'
#     n-=1
#
#     for row in l:
#         print(''.join(row)*num)