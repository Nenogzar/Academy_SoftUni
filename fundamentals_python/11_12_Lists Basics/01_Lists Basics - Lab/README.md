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


3.	List Statistics
On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
•	One with all the positives (including 0) numbers
•	One with all the negatives numbers
Finally, print the following message:</br>
**Count of positives: {count_positives}</br>
Sum of negatives: {sum_of_negatives}**

* Example

| Input | Output |
|-------|--------|
|5</br>10</br>3</br>2</br>-15</br>-4|[10, 3, 2]</br>[-15, -4]</br>Count of positives: 3</br>Sum of negatives: -19|

 | Input | Output                                                                             | 
 |-------|------------------------------------------------------------------------------------|
|6</br>11</br>2</br>35</br>599</br>31</br>20</br>| [11, 2, 35, 599, 31, 20]</br>[ ]</br>Count of positives: 6</br>Sum of negatives: 0 |

* Code:


    n = int(input())
    
    positive_numbers = []
    negative_numbers = []
    
    for _ in range(n):
        number = int(input())
    
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
        
        # or  positive_numbers.append(number) if number >= 0 else negative_numbers.append(number)
        
    print(positive_numbers)
    print(negative_numbers)
    print('Count of positives:', len(positive_numbers))
    print('Sum of negatives:', sum(negative_numbers))


or from  CEO

    number_range = int(input())
    
    list_plus = list()
    list_minus = list()
    minus_count = 0
    plus_count = 0
    
    for _ in range(number_range):
        number = int(input())
    
        if number >= 0:
            list_plus.append(number)
            plus_count += 1
    
        else:
            list_minus.append(number)
            minus_count += number
    
    print(f"{list_plus}\n{list_minus}")
    print(f"Count of positives: {plus_count}")
    print(f"Sum of negatives: {minus_count}")


4.	Search
On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings. You should add them to a list and print them. After that, you should filter out only the strings that include the given word and print that list too.

Example

| Input | Oyput |
|-------|-------|
|3</br>SoftUni</br>I study at SoftUni</br>I walk to work</br>I learn Python at SoftUni|["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]</br>["I study at SoftUni", "I learn Python at SoftUni"]</br>|
|4</br>tomatoes</br>I love tomatoes</br>I can eat tomatoes forever</br>I don't like apples</br>Yesterday I ate two tomatoes|["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]</br>["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]|


5.	Numbers Filter
On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:

•	even</br>
•	odd</br>
•	negative</br>
•	positive</br>
Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

**Example**

| Input                                          | Output        |
|------------------------------------------------|---------------|
| 5</br>33</br>19</br>-2</br>18</br>998</br>even | [-2, 18, 998] |
|       3</br>111</br>-4</br>0</br>negative</br> | [-4]          |


**Code:**


    n = int(input())
    exam_list = []
    sorted_list = []
    
    for n in range(n):
        input_num = int(input())
        exam_list.append(int(input_num))
    
    command = input().lower()
    
    if command == "even":
        sorted_list = [x for x in exam_list if x % 2 == 0]
    
    if command == "odd":
        sorted_list = [x for x in exam_list if x % 2 != 0]
    
    if command == "negative":
        sorted_list = [x for x in exam_list if x < 0]
    
    if command == "positive":
        sorted_list = [x for x in exam_list if x >= 0]
    
    print(sorted_list)


or  from CEO


    numbers = [int(input()) for _ in range(int(input()))]
    command = input()
    print([x for x in numbers if any([command == "odd" and x % 2 != 0,
                                      command == "even" and x % 2 ==0,
                                      command == "positive" and x >= 0,
                                      command == "negative" and x < 0])])
    
    
    
    
    numbers = [int(input()) for _ in range(int(input()))]
    data_ = {
        "odd": [x for x in numbers if x % 2 != 0],
        "even": [x for x in numbers if x % 2 == 0],
        "positive": [x for x in numbers if x >= 0],
        "negative": [x for x in numbers if x < 0]
    }
    print(data_[input()])


or 


    number_range = int(input())
    
    even = list()
    negative = list()
    positive = list()
    odd = list()
    
    for _ in range(1, number_range + 2):
        number = input()
    
        if number == "even":
            break
        elif number == "negative":
            break
    
        elif number == "positive":
            break
    
        elif number == "odd":
            break
    
        if int(number) % 2 == 0:
            even.append(int(number))
    
        if int(number) < 0:
            negative.append(int(number))
    
        if int(number) >= 0:
            positive.append(int(number))
    
        if int(number) % 2 != 0:
            odd.append(int(number))
    
    if number == "even":
        print(even)
    
    elif number == "negative":
        print(negative)
    
    elif number == "positive":
        print(positive)
    
    elif number == "odd":
        print(odd)


or from zahariev-webbersof

    n = int(input())
    COMMAND_EVEN = 'even'
    COMMAND_ODD = 'odd'
    COMMAND_NEGATIVE = 'negative'
    COMMAND_POSITIVE = 'positive'
    
    numbers = [int(input()) for _ in range(n)]
    filtered_numbers = []
    
    command = input()
    
    for num in numbers:
        filtered_command = ((command == COMMAND_EVEN and num % 2 == 0) or
                            (command == COMMAND_ODD and num % 2 != 0) or
                            (command == COMMAND_POSITIVE and num >= 0) or
                            (command == COMMAND_NEGATIVE and num < 0)
        )
    
        if filtered_command:
            filtered_numbers.append(num)
    
    print(filtered_numbers)


