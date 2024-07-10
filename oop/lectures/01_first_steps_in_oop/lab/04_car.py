#################################### TASK CONDITION ############################
'''
https://judge.softuni.org/Contests/Practice/Index/1934#3
4.	Car
Create a class called Car. Upon initialization it should receive a name,
model and engine (all strings). Create a method called get_info()
 =which will return a string in the following format:
"This is {name} {model} with engine {engine}".

_______________________________________________
Example_01

Test Code	(no input data in this task)

car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

Output
This is Kia Rio with engine 1.3L B3 I4

'''

""" 1 """
class Car:
    def __init__(self,name:str,model:str, engine:str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self) -> str:
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")

print(car.get_info())


""" 2 """

class Car:

    def __init__(self, *data):
        [self.name,
         self.model,
         self.engine
         ] = data

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


# Part below is part from automatic judge system from SoftUni
car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
