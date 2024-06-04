# ******* Python Advanced Exam - 17 February 2024 ******* #

# *******  01_chicken_snack  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/4527#0

Henry loves street food and he can't wait for the weekend to come because that's when he goes for
a walk and enjoys his favorite food.
His mother knows this and decides to surprise him by putting some change in his pants pocket.

On the first line,
    you will be given a sequence of integers representing the amount of money in Henry's pocket.
In the next line,
    you will be given another sequence of integers representing the prices of foods that Henry can buy.

Henry has gone to his favorite fast food place, fumbles in his pocket, and pulls out some change.
You have to start with the last element from the amount of money sequence and
    compare it with the first element from the prices sequence.

· If their values are equal,
        Henry buys the food.
            After that, you should remove both of them from their sequences.
· If the amount of money is bigger than the price,
        he buys the food again,
            taking change (the difference between the amount of money and the price) and
            putting it in his pocket.

        You should calculate the difference between the values, and keep it.

        o Remove the current amount of money from its sequence and
            increase the next amount of money value in the sequence by the resulting difference you have calculated.
        o Remove the price from the prices sequence.

· If the amount of money is lower than the price remove both of them from their sequences.

You need to stop comparing when you have no more amounts of money or prices.

Input / Constraints
· On the first line, you will receive the integers, representing the amount of money size, separated by a single space.
· On the second line, you will receive the integers, representing the price size, separated by a single space.
· All given numbers will be valid integers in the range [1, 20].

Output

· The output of your program should be a single line of text, formatted according to the following rules:
    § If Henry managed to eat four or more foods print the following:
        o "Gluttony of the day! Henry ate {food count} foods."

    § If Henry has eaten some of the foods print the following:
        o "Henry ate: {food count} foods."
            · in case Henry has eaten only one food, print: "Henry ate: {food count} food."

    § If Henry has not eaten any food:
        o "Henry remained hungry. He will try next weekend again."


Examples

Input:

9 5 8 18
18 12 10 5
Output:
Henry ate: 2 foods.

Input:
18 10 8 9
5 10 12 18

Output:
Gluttony of the day! Henry ate 4 foods.

Input:
1 1 4 5 9 9 9
9 15 18 13 10

Output:
Henry ate: 1 food.

Input:
1 1 4 5 6 2 3 2
17 8 18 19 20

Output:
Henry remained hungry. He will try next weekend again
"""

##########: variant 1 :##########

from collections import deque

money_in_pocket = deque(map(int, input().split()))
prices_of_foods = deque(map(int, input().split()))
eat_foods = 0

while money_in_pocket and prices_of_foods:
    current_money = money_in_pocket.pop()
    food_price = prices_of_foods.popleft()

    if food_price <= current_money:
        eat_foods += 1
        current_money-=food_price

        if money_in_pocket:
            next_coins = money_in_pocket.pop()
            money_in_pocket.append(current_money + next_coins)
        else:
            money_in_pocket.append(current_money + next_coins)

    elif current_money == food_price:
        eat_foods += 1

if eat_foods < 1:
    print(f"Henry remained hungry. He will try next weekend again.")
elif eat_foods == 1:
    print(f"Henry ate: {eat_foods} food.")
elif eat_foods >= 4:
    print(f"Gluttony of the day! Henry ate {eat_foods} foods.")
else:
    print(f"Henry ate: {eat_foods} foods.")


##########: variant 2 :##########

from collections import deque

amount_of_money = [int(x) for x in input().split()]
price_of_foods = deque(int(x) for x in input().split())
foods = 0

while amount_of_money and price_of_foods:
    money = amount_of_money.pop()
    price = price_of_foods.popleft()

    if money < price:
        continue

    if money > price:
        change = money - price
        if amount_of_money:
            amount_of_money[-1] += change
    foods += 1

if not foods:
    print("Henry remained hungry. He will try next weekend again.")
elif foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")
else:
    print(f"Henry ate: {foods} food{'' if foods == 1 else 's'}.")

##########: variant 3 solution SoftUni :##########

from collections import deque

money = list(map(int, input().split()))
prices = deque(map(int, input().split()))

count = 0

while money and prices:
    current_money = money[-1]
    current_price = prices[0]

    if current_money == current_price:
        money.pop()
        prices.popleft()
        count += 1
    elif current_money > current_price:
        change = current_money - current_price
        money.pop()
        if money:
            money[-1] += change
        prices.popleft()
        count += 1
    else:
        money.pop()
        prices.popleft()


if count >= 4:
    print(f"Gluttony of the day! Henry ate {count} foods.")
elif count == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {count} food{'s' if count != 1 else ''}.")
