a = 5
b = '0'
c = 'x'.join(['ta', 'da'][::-1])
print(f"{c = }")
d = str(a) + b + c[2] + c.replace('x', '')

print(d)



# (Shakespeare)
s = "All that glitters is not gold"
print(s[9:-9])
print(s[::7])
print(s[:-4:-1])