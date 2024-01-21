import sys

n = int(input())
sum_odd = 0
sum_even = 0
oddmin = 10000000000.0
oddmax = -10000000000.0
evenmax = -10000000000.0
evenmin = 10000000000.0

for i in range(n):
    n1 = float(input())
    if i % 2 == 0:
        sum_odd += n1
        if oddmax < n1:
            oddmax = n1
        if oddmin > n1:
            oddmin = n1

    else:
        sum_even += n1
        if evenmax < n1:
            evenmax = n1
        if evenmin > n1:
            evenmin = n1

print(f"OddSum={sum_odd},")
print(f"OddMin={oddmin if oddmin != 10000000000.0 else 'No'},")
print(f"OddMax={oddmax if oddmax != -10000000000.0 else 'No'},")
print(f"EvenSum={sum_even},")
print(f"EvenMin={evenmin if evenmin != 10000000000.0 else 'No'},")
print(f"EvenMax={evenmax if evenmax != -10000000000.0 else 'No'}")
