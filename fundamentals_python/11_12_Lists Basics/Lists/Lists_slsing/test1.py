n = 79927398713
n = list(map(int,str(n)))
for i in range(len(n)-1,0,-2):
    n[i-1] = n[i-1]*2
    if n[i-1] > 9:
        n[i-1] = sum(list(map(int,str(n[i-1]))))
print(sum(n)%10 == 0)