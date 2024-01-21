page=int(input("Колко страници има книгата която трябва да прочетете? "))
pagetime=int(input("Колко станици прочитате за 1 час? "))
dayread=int(input("С какво време разполагате /бр. дни/? "))
totaltime = (page / pagetime) / dayread
print(f"Трябва да отделяте по {totaltime} часа на ден за да прочетете книга със {page} страници!")

hours = int(totaltime)  # Цялата част на часовете
minutes = int((totaltime * 60) % 60)  # Оставащите минути

print(f"Трябва да отделяте по {hours} часа и {minutes} минути на ден, за да прочетете книга с {page} страници!")
