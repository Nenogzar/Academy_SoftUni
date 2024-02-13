# Basic Syntax, Conditional Statements and Loops - Exercise
1.	Jenny's Secret Message
Jenny studies programming with Python and wants to create a program that greets the user when he/she gives his/her name.
The greeting should be in the format "Hello, {name}!".
However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!". Could you help her?

**code**


    name = input()
    if name == "Johnny":
        print("Hello, my love!")
    else:
        print(f"Hello, {name}!")


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


    age = int(input())
    drinks = ""
    
    if age <= 14:
        drinks = "toddy"
    elif age <= 18:
        drinks = "coke"
    elif age <=21:
        drinks = "beer"
    else:
        drinks = "whisky"
    
    print(f"drink {drinks}")


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


    message_number = int(input())
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
        print(message)


4.	Maximum Multiple
On the first line, you will be given a positive number, which will serve as a divisor. 
On the second line, you will receive a positive number that will be the boundary. 
You should find the largest integer N, that is:
•	divisible by the given divisor
•	less than or equal to the given bound
•	greater than 0
Note: it is guaranteed that N is found.

**code**


    divisor = int(input())
    boundary = int(input())
    
    result = (boundary // divisor) * divisor
    print(result)


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


    total_price = 0
    
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
    
    print(f"Total: ${total_price:.2f}")


6.	String Pureness
You will be given the number n. After that, you'll receive different strings n times. 
Your task is to check if the given strings are pure, 
meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
•	If a string is pure, print "{string} is pure."
•	Otherwise, print "{string} is not pure!"

**code**  


    string_number = int(input())
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
            print(f"{my_string} is pure.")


 or 


    num_strings = int(input())
    
    for n in range(num_strings):
        my_string = input()
    
        contains_special_chars = any(char in my_string for char in [',', '.', '_'])
    
        if contains_special_chars:
            print(f"{my_string} is not pure.")
        else:
            print(f"{my_string} is pure.")


| Input | Output|
|---------------------------------------------|---|
| 2</br>pure string</br>not_pure_string	      | pure string is pure.</br>not_pure_string is not pure!  |
| 3</br>SoftUni</br>12345</br>string.pureness | SoftUni is pure.</br>12345 is pure.</br>string.pureness is not pure!  |

	





7.	Double Char
You will be given strings until you receive the command "End". 
For each string given, you should print a string in which each character (case-sensitive) is repeated twice. 
Note that if you receive the string "SoftUni", you should NOT print it!

**code**


    for string_input in iter(input,"End"):
        if string_input != "SoftUni":
            doubled_string = ''.join(char * 2 for char in string_input)
            print(doubled_string)


|  Input: | Output: |
|---|---------|
|Hello World</br>Repeat</br>End|HHeelllloo</br>WWoorrlldd</br>RReeppeeaatt|





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


    needed_coffee = 0
    
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
        print(needed_coffee)


or 


    keywords = ["coding", "dog", "cat", "movie"]
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
        print(needed_coffee)


|  Input: | Output: |
|---|---------|
| dog</br>CAT</br>gaming</br>END| 3       |
|movie</br>CODING</br>MOVIE</br>CLEANING</br>cat</br>END|You need extra sleep|



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


    voldemort_flag = False
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
        print("Welcome to Hogwarts.")


| Input:  | Output:  |
|---|---|
| Luna</br>Hermione</br>Neville</br>Voldemort| Luna goes to Gryffindor.</br>Hermione goes to Hufflepuff.</br>Neville goes to Hufflepuff.</br>You must not speak of that name!</br>|




10.	'* Mutate Strings

You will be given **two strings**. 
* Transform the first string into the **second** one, **letter** by letter, starting from the first one. 
* After **each interaction**, print the **resulting** string only **if it is unique**.
**Note:** the strings will have the same length.

**code**


    second_text = input()
    
    for index in range(len(first_text)):
        if first_text[index] != second_text[index]:
            first_text = second_text[:index + 1] + first_text[index + 1:]
            print(first_text)


|  Input: |  Output:  |
|---|---|
| bubble gum</br>turtle hum  | tubble gum</br> turble gum</br> turtle gum</br> turtle hum  |



11. Easter Bread
Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
Create a program that calculates how many loaves you can make (according to the recipe) with the budget you have.
Here is the recipe for one loaf:

| Eggs  | 1 pack  |
|-------|---------|
| Flour | 1 kg    |
| Milk  | 0.250 l |

**First**, you will receive your budget. Then, you will receive the price for 1 kg flour.

The price for 1 pack of eggs is 75% of the price for 1 kg flour. 
The price for 1L milk is 25% more than the price for 1 kg flour. 
Keep in mind that you use only 250ml milk for a bread.

**Start** cooking the loaves and keep making them until you have enough budget. 
Keep in mind that:
* For every loaf of bread that you make, you will receive 3 colored eggs. 
* For every 3rd bread you make, you will lose some of your colored eggs 
after receiving the usual 3 colored eggs for your bread. 
* The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves - ({current_bread_count} - 2)

* In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left, formatted to the 2nd decimal place, in the following format:

"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."

**Input / Constraints**

* On the 1st line, you will receive the budget - a real number in the range [0.0…100000.0]
* On the 2nd line, you will receive the price for 1 kg flour - a real number in the range [0.0…100000.0]
* The input will always be in the correct format
* You will always have a remaining budget
* There will not be a case in which the eggs become a negative count
* 
**Output**
* In the end, print the number of loaves of Easter bread you have made, the colored eggs you have gathered, 
 and the money formatted to the 2nd decimal place in the format described above.


    budget = float(input())
    price_flour = float(input())
    price_egg_one_pack = 0.75 * price_flour
    price_l_milk = 1.25 * price_flour
    price_quarter_milk = price_l_milk * 0.25
    price_loaf = price_egg_one_pack + price_flour + price_quarter_milk
    colored_eggs = 0
    current_bread_count = 0
    money_left = budget
    
    while money_left >= price_loaf:
        current_bread_count += 1
        money_left -= price_loaf
        colored_eggs += 3
    
        if current_bread_count % 3 == 0:
            colored_eggs -= (current_bread_count - 2)
    
    print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")


| Input:  | Output:  |
|---|---|
| 100 <br/> 5  | You made 9 loaves of Easter bread! Now you have 15 eggs and 7.19BGN left.  |


12.	Christmas Spirit<br/>It is time to get in a Christmas mood.
<br/>You need to decorate the house in time for the big event, but you have limited days to do so.
<br/>Write a program that calculates how much money you will need to spend on Christmas decorations<br/> 
and how much your Christmas spirit will improve.
<br/>On the **first line**, you will receive the quantity of decorations you should buy each time you go shopping. 
<br/>On the second line, you will receive the days left until Christmas. 
<br/>There are 4 types of decorations, and each piece costs a certain price. <br/>
Also, each time you go shopping for a concrete type of decoration, your Christmas spirit is improved by some points:

| Decoration  | Price/<br/>Piece  | Points/<br/>Shopping |
|---|---|-----------------|
|  Ornament Set | 2$  | 5               |
|  Tree Skirt | 5$  | 3               |
| Tree Garland  |  3$ | 10              |
| Tree Lights | 15$  | 17              |


<Until Christmas, you go shopping for a certain decoration as follows:
* Every second day you buy Ornament Sets.
* Every third day you buy Tree Skirts and Tree Garlands.
* Every fifth day you buy Tree Lights. 
  * If you have bought Tree Skirts and Tree Garlands on the same day, you additionally increase your spirit by 30. <br/>
    * **Hint: A day happens to be the third one as well as the fifth one at the same time (for example the 15th day).**<br/>
  That's not all! You have a cat at home that really likes to mess around with the decorations:
* Every tenth day your cat ruins all tree decorations, and you lose 20 points of the spirit:
  * Because of that, you go shopping (for a second time during the day) to buy one piece of tree skirt, 
garlands, and lights, but you do NOT earn additional spirit points for them.
* Also, because of the cat - at the beginning of every eleventh day,
you are forced to increase the quantity of decorations needed to be bought each time you go shopping by adding 2.
* If the last day is the tenth day, the cat demolishes even more and ruins the Christmas turkey, 
and you lose an additional 30 points of spirit.
    In the end, you must print the total cost and the gained spirit.

Output
In the end, print the **total cost** and the total gained **spirit** in the following format:
* "Total cost: {budget}"
  * "Total spirit: {totalSpirit}"


    quantity = int(input())
    days = int(input())
    ornament_set = 2
    tree_skirt = 5
    tree_garlands = 3
    tree_lights = 15
    total_cost = 0
    gained_spirit = 0
    for day in range(1, days + 1):
        tree_set = False
        if day % 11 == 0:
            quantity += 2
        if day % 2 == 0:
            total_cost += ornament_set * quantity
            gained_spirit += 5
        if day % 3 == 0:
            total_cost += (tree_skirt + tree_garlands) * quantity
            tree_set = True
            gained_spirit += 13
        if day % 5 == 0:
            total_cost += tree_lights * quantity
            gained_spirit += 17
            if tree_set:
                gained_spirit += 30
        if day % 10 == 0:
            total_cost += tree_skirt + tree_garlands + tree_lights
            gained_spirit -= 20
    if days % 10 == 0:
        gained_spirit -= 30
  
    print(f"Total cost: {total_cost}")
    print(f"Total spirit: {gained_spirit}")



| Input:     | Output:                                |
|------------|----------------------------------------|
| 1 <br/> 7  | Total cost: 37 <br/>Total spirit: 58   |
| 3 <br/> 20 | Total cost: 558 <br/>Total spirit: 156 |