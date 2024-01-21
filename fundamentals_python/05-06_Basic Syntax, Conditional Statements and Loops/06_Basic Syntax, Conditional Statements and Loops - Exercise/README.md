# Basic Syntax, Conditional Statements and Loops - Exercise
1.	Jenny's Secret Message
Jenny studies programming with Python and wants to create a program that greets the user when he/she gives his/her name.
The greeting should be in the format "Hello, {name}!".
However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!". Could you help her?

**code**

    `name = input()
    if name == "Johnny":
        print("Hello, my love!")
    else:
        print(f"Hello, {name}!")`

2.	Drink Something
Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky. 
Create a program that receives a person's age and prints what he/she drinks.
Rules:
A kid is defined as someone under or at the age of 14.
A teen is defined as someone under or at the age of 18.
A young adult is defined as someone under or at the age of 21.
An adult is defined as someone above the age of 21.
Note: All the values are inclusive except the last one!

**code**

    `age = int(input())
    drinks = ""
    
    if age <= 14:
        drinks = "toddy"
    elif age <= 18:
        drinks = "coke"
    elif age <=21:
        drinks = "beer"
    else:
        drinks = "whisky"
    
    print(f"drink {drinks}")`


3.	Chat Codes
Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes. 
He starts by creating a program for only four messages. 
Create a program that receives the n number of messages sent. On the following n lines, it will receive integer numbers. 
For each number, the program should print a different message:
•	If the number is 88 - "Hello"
•	If the number is 86 - "How are you?"
•	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
•	If the number is over 88 - "Bye."

**code** 

    `message_number = int(input())
    message = ""
    for _ in range(message_number):
        code = int(input())
    
        if code == 88:
            message = "Hello"
        elif code == 86:
            message = "How are you?"
        elif code < 88:
            message = "GREAT!"
        else:
            message = "Bye."
        print(message)`


4.	Maximum Multiple
On the first line, you will be given a positive number, which will serve as a divisor. 
On the second line, you will receive a positive number that will be the boundary. 
You should find the largest integer N, that is:
•	divisible by the given divisor
•	less than or equal to the given bound
•	greater than 0
Note: it is guaranteed that N is found.

**code**

    `divisor = int(input())
    boundary = int(input())
    
    result = (boundary // divisor) * divisor
    print(result)`


5.	Orders
You work at a coffee shop, and your job is to place orders with the distributors. 
Thus, you want to know the price of each order. 

On the first line, you will receive integer N - the number of orders the shop will receive. 
For each order, you will receive the following information:
•	Price per capsule - a floating-point number in the range [0.01…100.00]
•	Days - integer in the range [1…31]
•	Capsules, needed per day - integer in the range [1…2000]
For each order, you should print a single line in the following format:
•	"The price for the coffee is: ${price}"
If you do not receive a correct order (one or more of the values are not in the given range), 
you should ignore it and move to the next one.
After you go through all orders, you need to print the total price in the following format:
•	 "Total: ${total_price}"
Both the price of a coffee and the total price must be formatted to the second decimal place. 

**code**

    `total_price = 0
    
    n = int(input())
    
    for _ in range(n):
        price_per_capsule = float(input())
        days = int(input())
        capsules_per_day = int(input())
    
        # Validate the input ranges
        if not (0.01 <= price_per_capsule <= 100.00) or not (1 <= days <= 31) or not (1 <= capsules_per_day <= 2000):
    
            continue
    
        order_price = price_per_capsule * days * capsules_per_day
        total_price += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")
    
    print(f"Total: ${total_price:.2f}")`

6.	String Pureness
You will be given the number n. After that, you'll receive different strings n times. 
Your task is to check if the given strings are pure, 
meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
•	If a string is pure, print "{string} is pure."
•	Otherwise, print "{string} is not pure!"

**code**

    `string_number = int(input())
    special_chars = [',', '.', '_']
    contains_comma = False
    contains_dot = False
    contains_underscore = False
    
    for _ in range(string_number):
        my_string = input()
    
    
        for char in special_chars:
            if char in my_string:
                if char == ',':
                    contains_comma = True
                elif char == '.':
                    contains_dot = True
                elif char == '_':
                    contains_underscore = True
    
        if contains_comma or contains_dot or contains_underscore:
            print(f"{my_string} is not pure!")
        else:
            print(f"{my_string} is pure.")`


 or 


    `num_strings = int(input())
    
    for n in range(num_strings):
        my_string = input()
    
        contains_special_chars = any(char in my_string for char in [',', '.', '_'])
    
        if contains_special_chars:
            print(f"{my_string} is not pure.")
        else:
            print(f"{my_string} is pure.")`


7.	Double Char
You will be given strings until you receive the command "End". 
For each string given, you should print a string in which each character (case-sensitive) is repeated twice. 
Note that if you receive the string "SoftUni", you should NOT print it!

**code**

    `for string_input in iter(input,"End"):
        if string_input != "SoftUni":
            doubled_string = ''.join(char * 2 for char in string_input)
            print(doubled_string)`


8.	How Much Coffee Do You Need?
Everybody knows that you spend too much time awake during nighttime.
Your task is to define how much coffee you need to stay awake. 
Until you receive the command "END", you need to read commands on different lines. 
According to the commands, calculate the number of coffees you need to drink to stay awake during the daytime.
The list of events can contain the following:

* You have homework to do ("coding").
* You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
* You watch a movie ("movie").
* If other events are present, they will be represented by arbitrary strings. Just ignore them!
Each event can be lowercase or uppercase:
  * If it is lowercase, you need 1 coffee by an event.
  * If it is uppercase, you need 2 coffees by an event.
  
In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".

**code**

    `needed_coffee = 0
    
    for command in iter(input, "END"):
        if command == "coding" or command == "dog" or command == "cat" or command == "movie":
            needed_coffee += 1
        elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
            needed_coffee += 2
        else:
            continue
    
        if needed_coffee > 5:
            print("You need extra sleep")
            break
    
    else:
        print(needed_coffee)`


or 


    `keywords = ["coding", "dog", "cat", "movie"]
    needed_coffee = 0
    
    for command in iter(input, "END"):
        if command in keywords:
            needed_coffee += 1
        elif command in map(str.upper, keywords):
            needed_coffee += 2
        else:
            continue
    
        if needed_coffee > 5:
            print("You need extra sleep")
            break
    
    else:
        print(needed_coffee)`


9. Sorting Hat
Help out the sorting hat to sort the new students in the houses of Hogwarts. You will be receiving names until the command "Welcome!". The length of each name determines in which house the student is going:

* If the name is less than 5 chars, the student is going into Gryffindor
  * Print "{name} goes to Gryffindor."
* If the name is exactly 5 chars, the student is going into Slytherin
  * Print "{name} goes to Slytherin."
* If the name is exactly 6 chars, the student is going into Ravenclaw
  * Print "{name} goes to Ravenclaw."s
* If the name is more than 6 chars, the student is going into Hufflepuff
  * Print "{name} goes to Hufflepuff."

While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program. No more sorting for today!
  If all students are sorted successfully, print "Welcome to Hogwarts."

**code**

    `voldemort_flag = False
    name = input()
    
    while name != "Welcome!":
        if name == "Voldemort":
            print("You must not speak of that name!")
            voldemort_flag = True
            break  # Прекратява изпълнението на кода, ако се въведе "Voldemort"
    
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")
    
        name = input()
    
    if not voldemort_flag:
        print("Welcome to Hogwarts.")`

