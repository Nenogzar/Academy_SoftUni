# # class Purchase:
# #     def __init__(self, product_name, cost):
# #         self.product_name = product_name
# #         self.cost = cost
# #
# #     def __add__(self, other):
# #         name = f'{self.product_name}, {other.product_name}'
# #         cost = self.cost + other.cost
# #         return Purchase(name, cost)
# #
# #
# # first_purchase = Purchase('sofa', 650)
# # second_purchase = Purchase('table', 150)
# # result = first_purchase + second_purchase
# # print(result.product_name)  # sofa, table; 800
# # print(result.cost)
#
#
# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __gt__(self, other):
#         return self.salary > other.salary
#
#     # def __add__(self, other):
#     #     return self.salary + other.salary
#
# person_one = Person('John', 20)
# person_two = Person('Natasha', 36)
# print(person_one > person_two)  # False
#
# print(person_one.salary > person_two.salary )
#
# print(person_one.salary + person_two.salary)

class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, ImageArea):
            return self.get_area() == other.get_area()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

class Person:
    def __init__(self, age):
        self.age = age

##########: TEST CODE :##########

# 1
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

p1 = Person(71)

print(a1.get_area() >= p1.age)
