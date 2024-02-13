version = int(input().replace('.', ''))
new_version = ".".join(str(version+1))
print(new_version)

"""  2  """

version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) -1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index -1] += 1
print(".".join(str(digit) for digit in version))


""" 3 """

program_version = [int(n) for n in input().split(".")]

new_version = program_version.copy()

if new_version[-1] + 1 > 9:
    new_version[1] = new_version[1] + 1
    new_version[2] = 0

else:
    new_version[2] = new_version[2] + 1

if new_version[1] + 1 > 10:
    new_version[0] = new_version[0] + 1
    new_version[1] = 0

print(f"{new_version[0]}.{new_version[1]}.{new_version[2]}")