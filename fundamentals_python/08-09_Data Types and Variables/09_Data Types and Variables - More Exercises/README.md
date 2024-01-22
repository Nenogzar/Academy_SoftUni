# Data Types and Variables - More Exercises
1.	Exchange Integers </br>
Read two integer numbers and, after that, exchange their values. Print the variable values before and after the exchange, as shown below:
* Examples

| Input      | Output                                                              |
|------------|---------------------------------------------------------------------|
| 5 <br/> 10 | Before: <br/>a = 5 <br/>b = 10 <br/> After:<br/> a = 10<br/>b = 5   |
| 10<br/>20  | Before: <br/>a = 10 <br/>b = 20 <br/> After:<br/> a = 20<br/>b = 10 |

**Hints**</br>
You may use a temporary variable to remember the old value of a, then assign the value of b to a, 
and then assign the value of the temporary variable to b.</br>
**code**

    number_one = int(input())
    number_two = int(input())
    
    print(f"Before:\na = {number_one}\nb = {number_two}")
    print(f"After:\na = {number_two}\nb = {number_one}")


or

    number_one = int(input())
    number_two = int(input())
    
    print(f"Before:\na = {number_one}\nb = {number_two}")
    
    number_one, number_two = number_two, number_one
    
    print(f"After:\na = {number_one}\nb = {number_two}")



2.	Prime Number Checker</br>
Write a program to check if a number is **prime**. A prime number is a natural number greater than 1, 
not a product of two smaller natural numbers. For example, 
the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
The **input** comes as an integer number.
The **output** should be **True** if the number is prime and **False** otherwise.</br>

Examples

| Input | Output |
|-------|--------|
| 7     | True   |
| 8     | False  |  
| 81    | False  | 


**code**

    n = int(input())
    
    if n > 1:
        for i in range(2, n // 2):
            if (n % i) == 0:
                print("False")
                break
        else:
            print("True")

or 

    n = int(input())
    
    # Check if n is a prime number
    if n > 1:
        for i in range(2, n // 2 + 1):
            if (n % i) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")


3.	Decrypting Messages
On the first line, you will receive a key (integer). On the second line, you will receive n – the number of lines, which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.
You should add the key to each of the characters and append them to a message. In the end, print the decrypted message. 

Examples

| Input                                             | Output  | Input                                             | Output  | 
|---------------------------------------------------|---------|---------------------------------------------------|---------|
| 3<br/>7<br/>P<br/>l<br/>c<br/>q<br/>R<br/>k<br/>f | SoftUni | 1<br/>7<br/>C<br/>d<br/>b<br/>q<br/>x<br/>o<br/>s | Decrypt |

**code**

    key = int(input())
    line = int(input())
    
    word = list()
    
    for _ in range(line):
        letter = input()
    
        to_check = ord(letter) + key
        word.append(chr(to_check))
    
    for letter in word:
        print(letter, end="")

or

    key = int(input())
    line = int(input())
    
    word = list()
    
    for _ in range(line):
        letter = input()
        word.append(chr(ord(letter) + key))
    
    print(*word, sep="")

4.	Balanced Brackets</br>
On the first line, you will receive n – the number of lines, which will follow. 
On the following n lines, you will receive one of the following:</br>
* Opening bracket – "(",</br>
* Closing bracket – ")" or</br>
* Random string</br>
Your task is to find out if the **brackets** are **balanced**. 
That means after every **opening** bracket should follow a **closing** one. 
Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, 
the expression should be marked as unbalanced. 
You should print "**BALANCED**" if the parentheses are balanced and "**UNBALANCED**" otherwise.

Examples

| Input                                                        | Output  | Input                                                | Output     | 
|--------------------------------------------------------------|---------|------------------------------------------------------|------------|
| 8<br/>(<br/>5 + 10<br/>)<br/>* 2 +<br/>(<br/>5<br/>)<br/>-12 | BALANCE | 6<br/>12 *<br/>)<br/>10 + 2 -<br/>(<br/>5 + 10<br/>) | UNBALANCED |

**code**

    number = int(input())
    counter = 0
    for _ in range(number):
        check = input()
        if "(" in check:
            counter += 1
        elif ")" in check:
            counter -= 1
        if 0 != counter != 1:
            print("UNBALANCED")
            break
    else:
        print("BALANCED")