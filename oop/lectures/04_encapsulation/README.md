<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">

|<a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/oop">Back to Python OOP</a>|||
|-|-|-|



Какво е encapsulation?
Капсулацията е един от основните принципи на обектно-ориентираното програмиране (OOP). Тя включва скриването на вътрешното състояние на обекта и предоставянето на достъп до него чрез публични методи. Това помага за защитата на данните и осигурява контрол върху начина, по който те се използват и модифицират.

Предимства на капсулацията
Контрол над данните: Можем да контролираме как данните се модифицират.
Скриване на данните: Скрити данни не могат да бъдат променени директно от външния код.
Гъвкавост и лесна поддръжка: Лесно можем да променим имплементацията, без да засягаме външния код.
Как се реализира капсулацията в Python?
В Python капсулацията се реализира чрез използване на приватни и публични атрибути и методи. Публичните атрибути и методи са достъпни извън класа, докато приватните са скрити.

Публични атрибути и методи
Атрибутите и методите, които започват с една или повече подчертавки (_ или __), са индикация, че те не трябва да се използват директно извън класа.

```py
class Car:
    def __init__(self, make, model):
        self.make = make  # Публичен атрибут
        self.model = model  # Публичен атрибут

    def display_info(self):
        print(f"Car make: {self.make}, model: {self.model}")  # Публичен метод

car = Car("Toyota", "Corolla")
car.display_info()  # Достъп до публичен метод и атрибути

```
Частни атрибути и методи
За да създадем приватен атрибут или метод, използваме двойно подчертаване __ пред името на атрибута или метода.


```py
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Приватен атрибут
        self.__model = model  # Приватен атрибут
        self.__year = year  # Приватен атрибут

    def display_info(self):
        print(f"Car make: {self.__make}, model: {self.__model}, year: {self.__year}")  # Публичен метод

    def __update_year(self, year):  # Приватен метод
        self.__year = year

car = Car("Toyota", "Corolla", 2020)
car.display_info()

# car.__make  # Ще даде грешка, защото е приватен атрибут
# car.__update_year(2021)  # Ще даде грешка, защото е приватен метод

```


Достъп до приватни атрибути и методи
Въпреки че директният достъп до приватни атрибути и методи не е разрешен, можем да създадем публични методи (getter и setter), които да предоставят достъп до тях.

```py
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def display_info(self):
        print(f"Car make: {self.__make}, model: {self.__model}, year: {self.__year}")

    # Getter за година
    def get_year(self):
        return self.__year

    # Setter за година
    def set_year(self, year):
        if year > 1885:  # Проверка за валидна година (първата кола е създадена около 1886)
            self.__year = year
        else:
            print("Invalid year")

car = Car("Toyota", "Corolla", 2020)
car.display_info()
print("Year:", car.get_year())

car.set_year(2021)
print("Updated year:", car.get_year())

car.set_year(1800)  # Невалидна година

```
Заключение
Капсулацията е важен принцип в OOP, който помага за защита и управление на данните в нашите програми. Чрез използването на публични и приватни атрибути и методи можем да контролираме достъпа до данните и да осигурим тяхната коректност и сигурност.

Ако имаш допълнителни въпроси или искаш примери за други концепции, свързани с OOP, не се колебай да попиташ!
</body>
