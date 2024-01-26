# Exercie: Lists Basics

[judge](https://judge.softuni.org/Contests/1725)</br>
[pastebin](https://pastebin.com/PqwhU2km) Ivan Shopov

1.	Invert Values</br>
Write a program that receives a single string containing positive and negative numbers separated by a single space.</br>>
Print a list containing the opposite of each number.

**Example**

| Input | Output | Input | Output |
|-------|--------|-------|--------|
|1 2 -3 -3 5|[-1, -2, 3, 3, -5]|-4 0 2 57 -101|[4, 0, -2, -57, 101]|


* **Code**


    numbers = input()
    
    lst = numbers.split(' ')
    new_list = list()
    
    for number in lst:
        result = int(number) * -1
        new_list.append(result)
    
    print(new_list)


**or**


    lst = numbers.split(' ')
    new_list = list()
    for number in lst:
    
        if number[0] == "-":
            new_list.append(abs((int(number))))
        else:
            new_number = int(str("-" + number))
            new_list.append(new_number)
    
    print(new_list)

**or**

    invert_list = [-int(x) for x in input().split()]
    print(invert_list)

**or**

    print([int(x) * - 1 for x in input().split()])


2.	Multiples List
Write a program that receives two numbers (factor and count). </br>
It should create a list with a length of the given count that contains only integer numbers, 
which are multiples of the given factor. </br>
The numbers should be only positive, and they should be arranged in ascending order, 
starting from the value of the factor.

**Example**

| Input | Output | Input    | Output |
|-------|--------|----------|--------|
|2</br>5|[2, 4, 6, 8, 10]| 1</br>10 |[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]|


**Code**


    numner_one = int(input())
    numner_two = int(input())
    
    print_text = list()
    
    for number in range(1, numner_two + 1):
        print_text.append(number * numner_one)


**or**


    x = int(input())
    y = int(input())
    new_list=[]
    for n in range(x, x*y+1, x):
        new_list.append(n)


**or** 


    x, y = int(input()), int(input())
    new_list = [n for n in range(x, x*y+1, x)]
    print(new_list)


**or** 


    numner_one = int(input())
    numner_two = int(input())
    
    print([x * numner_one for x in range(1, numner_two + 1)])


3. Football Cards</br>
Most football fans love it for the goals and excitement. </br>
Well, this problem does not. You are up to handle the referee's little notebook and 
count the players who were sent off for fouls and misbehavior.
The rules:</br>

   *  **Two teams**, named "A" and "B" have 11 players each. </br>
   * **The players** on each team are numbered from 1 to 11. </br>
   * Any player may be sent off the field by being given a **red card**. </br>
   * If one of the teams has less than 7 players remaining, the referee stops the game immediately, 
   and the team with less than 7 players loses.</br></br>
   The card is a string with the team's letter **("A" or "B")** followed by a single dash and the player's number. e.g., 
   the card **"B-7"** means player #7 from team B received a card.</br>
   
The task: You will be given a sequence of cards (could be empty), separated by a single space. 
You should print the count of remaining players on each team at the end of the game in the format: 
**"Team A - {players_count}; Team B - {players_count}"**. </br>
If the referee terminated the game, print an additional line: **"Game was terminated".**
   Note for the random tests: If a player who has already been sent off receives another card - ignore it.

**Example**

| Input | Otput | Input | Output                                      |
|-------|-------|-------|---------------------------------------------|
|A-1 A-5 A-10 B-2|Team A - 8; Team B - 10|A-1 A-5 A-10 B-2 A-10 A-7 A-3| Team A - 6; Team B - 10 Game was terminated |

**Code**
    letters = "AB"
    numbers = list(range(1, 12))
    combined_list = [f"{letter}-{num}" for letter in letters for num in numbers]
    remaining_a = 11
    remaining_b = 11
    
    user_input = input().split()
    
    for item in user_input:
        if item in combined_list:
            combined_list.remove(item)
            if item.startswith("A"):
                remaining_a -= 1
            else:
                remaining_b -= 1
        if remaining_a <= 6 or remaining_b <= 6:
            print(f"Team A - {remaining_a}; Team B - {remaining_b}")
            print("Game was terminated")
            break
    
    else:
        print(f"Team A - {remaining_a}; Team B - {remaining_b}")


**or**


    team_a_players = set(range(1, 11+1))
    team_b_players = set(range(1, 11+1))
    cards = input().split()
    
    for card in cards:
        team, player = card.split('-')
        player = int(player)
    
        if team == 'A' and player in team_a_players:
            team_a_players.remove(player)
        elif team == 'B' and player in team_b_players:
            team_b_players.remove(player)
        remaining_team_a = len(team_a_players)
        remaining_team_b = len(team_b_players)
    
        if len(team_a_players) < 7 or len(team_b_players) < 7:
            print(f"Team A - {remaining_team_a}; Team B - {remaining_team_b}")
            print("Game was terminated")
            break
    
    else:
        print(f"Team A - {remaining_team_a}; Team B - {remaining_team_b}")

4.	Number Beggars</br> 
You will receive 2 lines of input. On the first line, you will receive a single string of integers, 
separated by a comma and a space ", ".</br> 
On the second line, you will receive a count of beggars.</br> 
Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns, 
from the first to the last number in the list.</br>
For example:</br> 
[1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5], 
the second one collects [2, 4].</br> 
The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3, 
as they will respectively take [1, 4], [2, 5], and [3].</br>
Also, note that not all beggars have to take the same amount of "offers", meaning that the length 
of the list is not necessarily a multiple of n. The list length could be even shorter - i.e., 
the last beggars will take nothing (0).

**Example**

| Input | Output |
|-------|--------|
|1, 2, 3, 4, 5</br>2|[9, 6]|
|3, 4, 5, 1, 29, 4</br>6|[3, 4, 5, 1, 29, 4]|
|100, 94, 24, 99</br>5|[100, 94, 24, 99, 0]|

**Code:**


      first_line = input()
      second_line = int(input())
      
      first_line = first_line.split(",")
      total_list = list()
      old_list = list()
      length_of_first = len(first_line)
      
      if length_of_first < second_line:
          for number in first_line:
              total_list.append(int(number))
          for number in range(abs(length_of_first - second_line)):
              total_list.append(0)
      
      
      elif length_of_first == second_line:
          for number in first_line:
              total_list.append(int(number))
      
      else:
          for number in first_line:
              old_list.append(int(number))
          for _ in range(0, second_line):
              total_list.append(sum(old_list[_::second_line]))
      
      print(total_list)

or whit index[]


      beggars_list = input().split(",")
      beggars_list = [int(num) for num in beggars_list]
      range_beggars = int(input())
      sum_parts = [0] * range_beggars
      
      for i, num in enumerate(beggars_list):
          index = i % range_beggars
          sum_parts[index] += num


5.	Faro Shuffle</br>
A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.</br> 
Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on 
the bottom and the original top card is still on top.</br>
For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, 
gives ['ace', 'four', 'two', 'five', 'three', 'six']</br>
Write a program that receives a single string (cards separated by space) and on 
the second line receives a count of faro shuffles that should be made.</br> 
Print the state of the deck after the shuffle.</br>
Note: The length of the deck of cards will always be an even number.

**Example**

| Input                    | Output |
|--------------------------|--------|
| a b c d e f g h</br>5    |['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']|
| one two three four</br>3 |['one', 'three', 'two', 'four']|


**Code**

      input_list = input().split()
      shuffles = int(input())
      
      for _ in range(shuffles):
          middle = len(input_list) // 2
          shuffled_list = []
      
          for i in range(middle):
              shuffled_list.append(input_list[i])
              shuffled_list.append(input_list[i + middle])
              #  this is equal to:  shuffled_list.extend([input_list[i], input_list[i + middle]])
          input_list = shuffled_list
      
      print(input_list)


**or**  Ivan Shopov code


      deck_of_cards = input().split()
      count_of_shuffles = int(input())
      for shuffle in range(count_of_shuffles):
          middle_of_the_deck = len(deck_of_cards) // 2
          left_part = deck_of_cards[:middle_of_the_deck]
          right_part = deck_of_cards[middle_of_the_deck:]
          deck_after_shuffling = []
          for card_index in range(len(left_part)):
              deck_after_shuffling.append(left_part[card_index])
              deck_after_shuffling.append(right_part[card_index])
          deck_of_cards = deck_after_shuffling
      print(deck_of_cards)

**or** CEO code

      cards = input().split()
      shuffle = int(input())
      
      lenght = len(cards)
      mid = int(lenght / 2)
      
      for i in range(shuffle):
          list = []
          for p in range(0, mid):
              list.append(cards[p])
              list.append(cards[mid])
              mid += 1
          cards = list
          mid = int(lenght / 2)
      
      print(list)

**or** CEO code


      cards = input().split()
      shuffle = int(input())
      middle_of_deck = len(cards) // 2
      
      for number_of_shuffle in range(shuffle):
          result_after_shuffle = []
          for mid_card, front_card in enumerate(range(middle_of_deck), middle_of_deck):
              result_after_shuffle.append(cards[front_card])
              result_after_shuffle.append(cards[mid_card])
          cards = result_after_shuffle.copy()
      
      print(cards)


**or** CEO code


      cards = input().split()
      shuffle = int(input())
      middle_of_deck = len(cards) // 2
      
      for number_of_shuffle in range(shuffle):
          cards = [c for pair in zip(cards[:middle_of_deck], cards[middle_of_deck:]) for c in pair]
      
      print(cards)


6.	Survival of the Biggest</br>
Write a program that receives a **list of integer** numbers (separated by a single space) and a number **n**.</br> 
The number n represents the **count of numbers to remov**e from the list.</br> 
You should remove the **smallest ones**, and then, you should print all the numbers that are left in the list, 
separated by a comma and a space **", "**.

**Example**

| Input              | Output |
|--------------------|--------|
| 10 9 8 7 6 5</br>3 |10, 9, 8|
| 1 10 2 9 3 8</br>2 |10, 9, 3, 8|


**Code**

      numbers = list(map(int,input().strip().split(" ")))
      how_many_numbers_to_remove = int(input())
      
      for _ in range(how_many_numbers_to_remove):
          numbers.remove(min(numbers))
      count = 1
      for num in numbers:
          if count != (len(numbers)):
              print(f"{num},", end=" ")
      
          else:
              print(f"{num}")
          count += 1

**or** code from CEO


      numbers = [int(num) for num in input().split()]
      n = int(input())
      
      for _ in range(n):
          numbers.remove(min(numbers))
          result = ', '.join(map(str, numbers))
      #print(numbers)
      print(result)


**or** code from CEO


      numbers = list(map(int,input().strip().split(" ")))
      how_many_numbers_to_remove = int(input())
      
      for n in range(how_many_numbers_to_remove):
          numbers.remove(min(numbers))
      print(", ".join(str(x) for x in numbers))


**or** code from CEO


      number = list(map(int, input().strip().split(" ")))
      [number.remove(min(number)) for _ in range(int(input()))]
      print(", ".join(str(x) for x in number))