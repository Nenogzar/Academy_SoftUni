1.	Number Definer
Write a program that reads a floating-point number and:
-	prints "zero" if the number is zero
-	prints "positive" or "negative"
-	adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
1 000 000

        input_number = float(input())
        if input_number ==0:
            print("zero")
        if input_number > 0:
            if input_number>100000:
                print("large positive")
            elif input_number < 1:
                print("small positive")
            else:
                print("positive")
        elif input_number < 0:
            if input_number > -1:
                print("small negative")
            elif input_number < -1000000:
                print("large negative")
            else:
                print("negative")


2.	Largest of Three Numbers
Write a program that receives three whole numbers and prints the largest one.


        num_list = []
        for _ in range(3):
            num_list.append(int(input()))
            max_num=max(num_list)
        print(max_num)


3.	Word Reverse
Write a program that receives a single word, reverses it, and prints it.


        reversed_word = ''.join(reversed(input()))
        print(reversed_word)


4.	Even Numbers
Write a program that receives a number n on the first line. On the following n lines, 
it receives different integer numbers. If the program receives an odd number, 
print "{num} is odd!" and end the program. Otherwise, if all numbers given are even, print "All numbers are even.".


        number = int(input())
        
        for _ in range(number):
            check_even = int(input())
            if not check_even % 2 == 0:  #  if check_even % 2 != 0:
                print(f"{check_even} is odd!")
                break
        else:
            print("All numbers are even.")


5.	Number Between 1 and 100
Write a program that reads different floating-point numbers from the console. 
When it receives a number between 1 and 100 inclusive, the program should stop reading and 
should print "The number {number} is between 1 and 100".


        while True:
            number = float(input())
            if 1 <= number <= 100:
                break
        
        print(f"The number {number} is between 1 and 100")


or


    for number in iter(lambda: float(input()), None):
        if 1 <= number <= 100:
            break
    
    print(f"The number {number} is between 1 and 100")


6.	Shopping
Write a program that reads an integer number representing a budget. 
On the following lines, it reads integer numbers representing the prices of each product 
you should buy until it receives the command "End".
During the iterations, if there is not enough budget left to buy the next product, 
it prints "You went in overdraft!" and end the program.
Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."


        budget = int(input())
        command = input()
        
        while command != "End":
            expense = int(command)
            budget -= expense
        
            if budget < 0:
                print("You went in overdraft!")
                break
            command = input()
        else:
            print("You bought everything needed.")


7.	Patterns
Write a program that receives a number and creates the following pattern. The number represents the largest count of stars on one row.


        n = int(input())
        
        for i in range(1, n*2):
            if i <= n:
                width = i
            else:
                width = n*2 - i
            print("*" * width)
