product = input().lower()  # Преобразуване на въведения текст в малки букви

# Проверка дали продуктът е плод, зеленчук или неизвестен
if product in ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]:
    category = "fruit"
elif product in ["tomato", "cucumber", "pepper", "carrot"]:
    category = "vegetable"
else:
    category = "unknown"

# Извеждане на категорията на продукта
print(category)
