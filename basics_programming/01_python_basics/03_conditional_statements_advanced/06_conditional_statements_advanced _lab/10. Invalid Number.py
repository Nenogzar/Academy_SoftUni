number = int(input("Въведете цяло число: "))

# Проверка дали числото не е в диапазона и не е 0, и ако не е, извеждаме "invalid"
if not ((100 <= number <= 200) or (number == 0)):
    print("invalid")