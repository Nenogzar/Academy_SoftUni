# Lab: Lists Basics

[judge](https://judge.softuni.org/Contests/1724)

1.	Strange Zoo
You are at the zoo, and the meerkats look strange. 
You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. Your task is to re-arrange the elements in a list so that the animal looks normal again:
•	On the first position is the head;
•	On the second position is the body;
•	On the last one is the tail.

| Input | Output |
|-------|--------|
|   my tail<br/>my body seems on place<br/>my head is on the wrong end!   | ['my head is on the wrong end!', 'my body seems on place', 'my tail'] |


| Input | Output | Input | Output |
|-------|--------|-------|--------|
|tail</br>body</br>head|['head', 'body', 'tail']|T</br>B</br>H|['H', 'B', 'T']|

* Hints</br>
We start by reading the three parts of the body:

  * Code


    head = input()
    body = input()
    tail = input()
    text = [tail, body, head]
    print(text)

or

    my_list = []
    
    for _ in range(3):
        data = input()
        my_list.append(data)
    my_list[0], my_list[2] = my_list[2], my_list[0]
    print(my_list)

or

    my_list1 = []
    
    for _ in range(3):
        data = input()
        my_list1.append(data)
    new_list = my_list1[::-1]
    print(new_list)

or

    my_list2 = []
    
    for _ in range(3):
        data = input()
        my_list2.append(data)
        new_list2 = my_list2.reverse()
    print(new_list2)


2.	Courses</br>
On the first line, you will receive a single number n. On the following n lines, you will receive names of courses. You should create a list of courses and print it.

| Input | Output |
|-------|--------|
|   2</br>PB Python</br>PF Python|   ['PB Python', 'PF Python']     |
|      4</br>Front-End</br>C# Web</br>JS Core</br>Programming Fundamentals |  ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']     |

Hints
We read the number n from the console, and we create an empty list:

* Code 


    course = []
    for i in range(int(input())):
        courses = input()
        course.append(courses)
    print(course)

or

    n = int(input())
    courses_list = []
    
    for _ in range(n):
        course_name = input()
        courses_list.append(course_name)
    
    print(courses_list)


