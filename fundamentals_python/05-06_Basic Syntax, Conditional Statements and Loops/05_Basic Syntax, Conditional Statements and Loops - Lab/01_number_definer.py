""" 1 """
float_number = float(input())
if float_number == 0:
    print("zero")

if float_number > 0:
    if float_number < 1:
        print('small positive')
    elif float_number > 1000000:
        print('larg positive')
    else:
        print('positive')

if float_number < 0:
    if abs(float_number) < 1:
        print('small negative')
    elif abs(float_number) > 1000000:
        print('larg negative')
    else:
        print('negative')




