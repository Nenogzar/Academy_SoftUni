# def squares(n):
#     current = 1
#     while current <= n:
#         yield current **2
#         current += 1

def squares(n):
    for i in range(1, n + 1):
        yield i * i



a = squares(5)
print(a)
print(list(a))

