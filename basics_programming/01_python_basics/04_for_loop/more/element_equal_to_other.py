n = int(input())
sum_elements = 0
max_element = float('-inf')  # Задаваме начална стойност за най-голямото число

for i in range(n):
    n1 = int(input())
    sum_elements += n1
    if n1 > max_element:  # Проверка за най-голямото число
        max_element = n1
    #print(f"{sum_elements} - sum_elements")
    #print(f"{max_element} - max_element")
    n2 = sum_elements - max_element
if max_element == n2:
    print(f"Yes\nSum = {n2:.0f}")
else:
    print(f"No\nDiff = {max_element - n2:.0f}")
