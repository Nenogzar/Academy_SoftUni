""" 1 """
name = input()

if name == "Johnny":
    print("Hello, my love!")

else:
    print(f"Hello, {name}!")

""" 2 """
name1 = input()
if name1 == 'Johnny':
    name1 = 'my love'
print(f"Hello, {name1}!")

""" 3 """
name2 = input()
print("Hello, my love!" if name2 == 'Johnny' else f"Hello, {name2}!")

""" 4 """
name3 = input()
print(f"Hello, {name3}!" if name3 != 'Johnny' else "Hello, my love!")

""" ISch """
