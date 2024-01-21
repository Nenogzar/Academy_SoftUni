while True:

    animal = input("Напишете вид животно -/dog, crocodile, tortoise, snake/: ")
    a = "mammal"
    b = "reptile"
    animal_type = 0

    if animal == "dog":
        animal_type = "mammal"
    elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
        animal_type = " reptile"
    else:
        animal_type = "unknown"

    if animal != "":
        print(f"{animal} is from class {animal_type}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
