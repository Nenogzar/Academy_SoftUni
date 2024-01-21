import math

serial = input()
film_time = int(input())
break_time = int(input())
lunch_time = break_time / 8
relax_time = break_time / 4

watch_time = break_time - lunch_time - relax_time
free_time = math.ceil(film_time-watch_time)

print(f"You have enough time to watch {serial} and left with {math.ceil(watch_time - film_time)} minutes free time."
      if watch_time >= film_time else
      f"You don't have enough time to watch {serial}, you need {math.ceil(film_time-watch_time)} more minutes.'")
