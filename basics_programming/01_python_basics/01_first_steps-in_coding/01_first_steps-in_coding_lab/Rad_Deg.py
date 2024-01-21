import math

rad = float(input("Въведете ъгъл в радиани: "))
deg = rad * 180 / math.pi  # Преобразуване на радиани в градуси
deg_floor = math.floor(deg)  # Закръгляне на градусите надолу

print(f"Градусите са: {deg_floor}")

