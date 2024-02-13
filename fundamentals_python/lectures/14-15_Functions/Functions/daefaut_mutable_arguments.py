"""A default arguments is a mutable object like 'list' in our case,
 Python creates it when you define the function,
 and not every time you invoke it."""
def func(default_arg=[]):
    default_arg.append('SoftUni')
    return default_arg

#obj = list(map(str, input("Enter a string: ").split()))

for num in range(1, 3):
    print(f"{num}: {func()}")
