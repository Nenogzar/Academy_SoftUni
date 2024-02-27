# Objects and Classes - Exericse

[judge](https://judge.softuni.org/Contests/1734)

## 01. Storage

<details> <summary>👈Code 🐍 </summary>

```Python
class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > len(Storage.storage):
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage

```

</details>

## 2.	Weapon

<details> <summary>👈Code 🐍 </summary>

```Python
class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

```

</details>

## 3.	Catalogue

<details> <summary>👈Code 🐍 </summary>

```Python
class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.products))
        return returning_string

```

</details>

## 4.	Town

<details> <summary>👈Code 🐍 </summary>

```Python
class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude: str) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude: str) -> None:
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

```

</details>

## 5.	Class

<details> <summary>👈Code 🐍 </summary>

```Python
class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return float(f"{average_grade:.2f}")

    def __repr__(self):
        students = ", ".join(self.students)
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {students}. Average grade: {average_grade}"

```

</details>

## 6.	Inventory

<details> <summary>👈Code 🐍 </summary>

```Python
class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.left_over = 0

    def add_item(self, item: str):
        if self.left_over < self.__capacity:
            self.items.append(str(item))
            self.left_over += 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.get_capacity(self) - self.left_over}"

```

</details>

## 7.	Articles

<details> <summary>👈Code 🐍 </summary>

```Python
class Article:

    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_author: str):
        self.author = new_author

    def rename(self, new_title: str):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"

```

</details>

## 8.	* Vehicle

<details> <summary>👈Code 🐍 </summary>

```Python
class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        else:#elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner: #if self.owner is not None
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"

```
</details>

## 9.	* Movie

<details> <summary>👈Code 🐍 </summary>

```Python
class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched: # if self.watched == False
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"

```

</details>