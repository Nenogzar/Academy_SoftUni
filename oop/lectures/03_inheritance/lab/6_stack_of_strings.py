# ******* Inheritance - Lab ******* #

# *******  6_stack_of_strings  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1940#5

Create a class Stack that can store only strings and has the following functionality:
•	Instance attribute: data: list
•	Method: push(element) – adds an element at the end of the stack
•	Method: pop() – removes and returns the last element in the stack
•	Method: top() - returns a reference to the topmost element of the stack
•	Method: is_empty() - returns boolean True/False
•	Override the string method to return the stack data in the format:
"[{element(N)}, {element(N-1)} ... {element(0)}]"

"""

##########: SOLUTION :##########
class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()


    def top(self):
        if not self.is_empty():
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    #  def is_empty(self):
    #         if Stack.data:
    #             return False
    #         return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"






##########: TEST CODE :##########

# Създаване на нов стек
stack = Stack()

# Проверка дали стекът е празен
print(stack.is_empty())  # Очаквано: True

# Добавяне на елементи
stack.push("first")
stack.push("second")
stack.push("third")

# Печат на стека
print(stack)  # Очаквано: [third, second, first]

# Проверка на top метода
print(stack.top())  # Очаквано: third

# Премахване на елемент и проверка на стека
print(stack.pop())  # Очаквано: third
print(stack)  # Очаквано: [second, first]

# Проверка на top метода след pop
print(stack.top())  # Очаквано: second

# Проверка дали стекът е празен
print(stack.is_empty())  # Очаквано: False

# Премахване на всички елементи
print(stack.pop())  # Очаквано: second
print(stack.pop())  # Очаквано: first

# Проверка дали стекът е празен
print(stack.is_empty())  # Очаквано: True


"""
Output:

True
[third, second, first]
third
third
[second, first]
second
False
second
first
True
 """
##########: UNITTEST :##########


