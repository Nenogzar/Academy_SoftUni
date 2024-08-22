def genrange(start, end):
    for i in range(start, end+1):
        yield i



def genrange(start, end):
    while start <= end:
        yield start
        start +=1







a = genrange(1,10)

for el in a:
    print(el)
