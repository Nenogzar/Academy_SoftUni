A = list(k for k in range(1, 21) if k % 3 != 0)

B = [2 ** (k // 2) if k % 2 == 0 else 3 ** (k // 2) for k in range(15)]

C = [0 if k==0 or k==1 else k**2 for k in range(13) if not k in [2, 5, 7]]

alpha = A[::-1]
bravo = B[::2]
charly = B[1::2]




print(f"{A = }")
print(f"{B = }")
print(f"{C = }")
print(f"{alpha = }")
print(f"{bravo = }")
print(f"{charly = }")

