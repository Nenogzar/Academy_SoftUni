# float_number = float(input())
# if float_number == 0:
#     print("zero")
#
# if float_number == 0:
#     print('zero')
#
# if float_number > 0:
#     if float_number < 1:
#         print('small positive')
#     elif float_number > 1000000:
#         print('larg positive')
#     else:
#         print('positive')
# if float_number < 0:
#     if abs(float_number) < 1:
#         print('small negative')
#     elif abs(float_number) > 1000000:
#         print('larg negative')
#     else:
#         print('negative')

float_number = float(input())

if float_number == 0:
    print('zero')
elif 0 < float_number < 1:
    print('small positive')
elif float_number >= 1 and float_number <= 1000000:
    print('positive')
elif float_number > 1000000:
    print('large positive')
elif -1 <= float_number < 0:
    print('small negative')
elif float_number < -1000000:
    print('large negative')
else:
    print('negative')
