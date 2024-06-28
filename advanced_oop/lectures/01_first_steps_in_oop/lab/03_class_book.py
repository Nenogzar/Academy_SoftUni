#################################### TASK CONDITION ############################
'''
https://judge.softuni.org/Contests/Practice/Index/1934#2
3.	Class Book
Create a class called Book. It should have an __init__() method that should receive:
•	name: string
•	author: string
•	pages: int
Submit only the class in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

Output
My Book
Me
200

'''

class Book:

    def __init__(self, *books):
        [self.name,
         self.author,
         self.pages] = books
        # self.name = books[0]
        # self.author = books[1]
        # self.pages = int(books[2])


# Part below is part from automatic judge system from SoftUni
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


