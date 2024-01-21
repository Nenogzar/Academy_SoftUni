n = int(input())
sum_odd =0
sum_event =0

for i in range (0,n):
    n1 = int(input())
    if i % 2 ==0:
        sum_event+=n1
    else:
        sum_odd +=n1
if sum_odd == sum_event:
    print(f"Yes\nSum = {abs(sum_odd)}")
else:
    print(f"No\nDiff = {abs(sum_odd-sum_event)}")
