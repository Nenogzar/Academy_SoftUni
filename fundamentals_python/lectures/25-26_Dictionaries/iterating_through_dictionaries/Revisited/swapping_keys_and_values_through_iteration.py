numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

swapping_dict = {value: key for key, value in numbers.items()}
print(swapping_dict) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

############################################################

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week = {days_of_week[num]:num for num in range(len(days_of_week))}
print(week) # {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
swapping_week = {value:key for key, value in week.items()}
print(swapping_week) # {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

############################################################
new_week = dict.fromkeys(days_of_week, 0)
print(new_week)
