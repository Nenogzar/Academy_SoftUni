""" checking_usernames """
current_usernames = ['admin', 'dimo', 'dimitar', 'ivailo10', 'five']
new_usernames = ['pesho1', 'dimo', 'stamat40', 'pesho10', 'ivailo10']

for new_username in new_usernames:
    if new_username in current_usernames:
        print('Username has already been used')
    else:
        print('Username is available')

""" lilt_usernames """
usernames = ['admin', 'dimo', 'dimitar', 'ivailo10', 'five']

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would to like to see a status report')
        else:
            print(f'Hello {username}')
else:
    print('We need to find some user')

""" ordinal_numbers """
test = 0
numbers = 1, 2, 3, 4, 5, 6, 7, 8
for num in numbers:
    max_num = max(numbers)
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{max_num - num }')