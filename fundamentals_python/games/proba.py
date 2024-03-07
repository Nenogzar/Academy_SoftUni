from icecream import ic


# def multiply(a, b):
#     return a * b
#
#
# n, m = int(input()), int(input())
# result = ic(multiply(n, m))
# ic(multiply(50, 20))
# ic(multiply(20, 10))

""" dictionaty """
# data = {'data': [1,2,3,4,5],
#         'lable': ['a','b','c','d','e']}
#
# ic(data['data'][2], data['lable'][2])

"""  """

def multi(value):
    if value % 2 == 0:
        ic()
        return True
    else:
        return False

print(multi(10))
print(multi(11))
print(multi(12))
print(multi(13))

