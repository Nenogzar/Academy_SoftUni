number1 = int(input("Въведете първото число: "))
number2 = int(input("Въведете второто число: "))

for i in range(11):
    result1 = number1 * i
    result2 = number2 * i
    print(f"{number1} x {i} = {result1}, {number2} x {i} = {result2}")
