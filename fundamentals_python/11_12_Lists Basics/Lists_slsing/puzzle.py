a = 5
b = '0'
c = 'x'.join(['ta', 'da'][::-1])
print(c)
d = str(a) + b + c[2] + c.replace('x', '')
print(d)