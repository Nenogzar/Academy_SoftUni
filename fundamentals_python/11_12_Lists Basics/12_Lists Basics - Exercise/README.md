# Exercie: Lists Basics

[judge](https://judge.softuni.org/Contests/1725)</br>

[Pastebin Ivan Shopov](https://pastebin.com/PqwhU2km) </br>

[Code from kumchovylcho](https://github.com/kumchovylcho/softuni/blob/master/Fundamentals%20-%20Python/Lists_Basics%20-%20exercise)</br>

[Code from CEO](https://icode-example.ceo-py.eu/menu?language=Python&course=Fundamentals&module=Lists%20Basics%20-%20Exercise)

 
### 1. Invert Values</br>

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

    list_with_numbers = input().split()
    opposite_numbers = []
    for number in list_with_numbers:
        opposite_number = -int(number)
        opposite_numbers.append(opposite_number)
    print(opposite_numbers)


**or**

    invert_list = [-int(x) for x in input().split()]
    print(invert_list)

**or**

    print([int(x) * - 1 for x in input().split()])

**or**

    print([-int(number) for number in input().split()])


### 2.	Multiples List
Write a program that receives **two numbers** (factor and count). </br>
It should **create a list** with a **length of the given count** that contains only integer numbers, 
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


### 3. Football Cards</br>
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

**from IvanShopov**

    team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
    team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
    players = input().split()
    game_was_terminated = False
    for player in players:
        if player in team_a:
            team_a.remove(player)
        elif player in team_b:
            team_b.remove(player)
        if len(team_a) < 7 or len(team_b) < 7:
            game_was_terminated = True
            break
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    if game_was_terminated: #if game was terminated == True
        print("Game was terminated")

### 4.Number Beggars</br> 
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


### 5.	Faro Shuffle</br>
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


### 6.	Survival of the Biggest</br>
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
      
      for n in range(how_many_numbers_to_remove):
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


### 7. '* Easter Gifts</br>
_As a good friend, you decide to buy presents for your friends._</br>
Create a program that helps you plan the gifts for your friends and family. 
First, you are going to receive the gifts you plan on buying on a **single line**, **separated by space**, in the **following format**:</br>
**"{gift1} {gift2} {gift3}… {giftn}"**</br>
Then you will start receiving commands until you read the **"No Money"** message. There are **three** possible commands:</br>
   * **"OutOfStock {gift}"**</br>
     * **Find** the gifts with this name in your collection, if any, and change their values to "None".  </br>
   * **"Required {gift} {index}"**</br>
     * If the **index is valid**, replace the gift on the given index with the given gift. </br>
   * **"JustInCase {gift}"**</br>
     * **Replace** the value of your **last** gift with this one. </br>
In the end, print the gifts on a single line, except the ones with value **"None"**,
separated by a single space in the following format:</br>
     **"{gift1} {gift2} {gift3} … {giftn}"**</br>

**Input / Constraints**</br>
•	On the 1st line,  you will receive the names of the gifts, separated by a single space.</br>
•	On the following lines, until the "No Money" command is received, you will be receiving commands.</br>
•	The input will always be valid.</br>

**Output**</br>
•	Print the gifts in the format described above.

| Input                                  | Output                                     |
|----------------------------------------|--------------------------------------------|
| Eggs StuffedAnimal Cozonac Sweets</br>EasterBunny Eggs Clothes</br>OutOfStock Eggs</br>Required Spoon 2</br> JustInCase ChocolateEgg</br>No Money| StuffedAnimal Spoon Sweets EasterBunny<br>ChocolateEgg |

**Comments**</br>
First, we receive the command "**OutOfStock**", and we need to replace the values of "**Eggs**" with "**None**". 
After this command, the list should look like this:</br>
**None StuffedAnimal Cozonac Sweets EasterBunny None Clothes**</br>
Afterward, we receive the "Required" command, and we need to replace the value on the 2nd index 
of our list with the value "Spoon". The list should look like this:  </br>
**None StuffedAnimal Spoon Sweets EasterBunny None Clothes**</br>
After, we receive the "JustInCase" command, which means we need to replace the last value in 
our list with "ChocolateEggs". The list should look like this:</br>
**None StuffedAnimal Spoon Sweets EasterBunny None ChocolateEggs**</br> 
In the end, we print all of the gifts, except the ones with values "**None**". </br>
The final list: **StuffedAnimal Spoon Sweets EasterBunny ChocolateEggs**

| Input                                                                                                                                                                                    | Output |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Sweets Cozonac Clothes Flowers Wine</br> Clothes Eggs Clothes</br> Required Paper 8</br> OutOfStock Clothes</br> Required Chocolate 2</br> JustInCase Hat</br> OutOfStock Cable</br> No Money |Sweets Cozonac Chocolate Flowers Wine</br> Eggs Hat|

**Code**

      names_of_gifts = input().split(" ")
      #print(names_of_gifts)
      
      command = input()
      while command != "No Money":
          command_type, *other_info = command.split()
      
          if "OutOfStock" in command_type:
      
              for i, name in enumerate(names_of_gifts):
      
                  if other_info[-1] == name:
                      names_of_gifts[i] = "None"
      
          elif "Required" in command_type:
              length = len(names_of_gifts)
      
              if length > int(other_info[-1]) >= 0:
                  names_of_gifts[int(other_info[-1])] = other_info[0]
      
          elif "JustInCase" in command_type:
      
              names_of_gifts[-1] = other_info[-1]
          command = input()
      
      print(" ".join(x for x in names_of_gifts if x != "None"))


[Code from CEO](https://icode-example.ceo-py.eu/solution?desc=Python-Fundamentals-Lists-Basics-Exercise-07.-Easter-Gifts&id=658332b29f8515abe6963ae7)
      

      names_of_gifts = input().split(" ")
         
      command = input()
      while command != "No Money":
          command_type, *other_info = command.split()
          if "OutOfStock" in command_type:
              for i, name in enumerate(names_of_gifts):
                  if other_info[-1] == name:
                      names_of_gifts[i] = "None"
          elif "Required" in command_type:
              length = len(names_of_gifts)
              if length > int(other_info[-1]) >= 0:
                  names_of_gifts[int(other_info[-1])] = other_info[0]
          elif "JustInCase" in command_type:
              names_of_gifts[-1] = other_info[-1]
          command = input()
      
      print(" ".join(x for x in names_of_gifts if x != "None"))


[Code from kumchovylcho](https://github.com/kumchovylcho/softuni/blob/master/Fundamentals%20-%20Python/Lists_Basics%20-%20exercise/Easter_gifts.py)


      gifts = input().split()
      command = input()
      while command != "No Money":
          command = command.split()
          operation, current_gift = command[0], command[1]
          if operation == "OutOfStock":
              gifts = [None if gift == current_gift else gift for gift in gifts]
          elif operation == "Required":
              index = int(command[2])
              if 0 <= index < len(gifts):
                  gifts[index] = current_gift
          elif operation == "JustInCase":
              gifts[-1] = current_gift
          command = input()
      
      for gift in gifts:
          if gift is not None:
              print(f"{gift}", end=' ')



      gifts = input().split()
      command = input()
      while command != "No Money":
          list_with_commands = command.split()
          if list_with_commands[0] == "OutOfStock":
              for word in range(len(gifts)):
                  if gifts[word] == list_with_commands[1]:
                      gifts[word] = "None"
          elif list_with_commands[0] == "Required":
              for word in range(len(gifts)):
                  if word == int(list_with_commands[2]):
                      gifts[word] = list_with_commands[1]
          elif list_with_commands[0] == "JustInCase":
              gifts[-1] = list_with_commands[1]
          command = input()
      for words in gifts:
          if words != "None":
              print(words, end=" ")


### 8.	 Seize the Fire</br>
The group of adventurists has gone on their first task. Now they should walk through fire - literally. 
They should use all the water they have left. Your task is to help them survive.
Create a program that calculates the water needed to put out a **"fire cell"**, 
based on the given information about its **"fire level"** and how much it gets affected by water.
**First**, you will be given the **level of fire** inside the cell with the integer value of the cell,
which represents the needed water to put out the fire.  They will be given in the following format:</br>
**"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"**</br>
Afterward you will receive the amount of **water** you have for putting out the fires. 
There is a **range** of fire for each fire type, and if a cell's value is **below or exceeds it**, it is invalid, 
and you do not need to put it out.</br>
Type of Fire	Range</br>
High	81 - 125</br>
Medium	51 - 80</br>
Low	1 - 50</br>
If a cell is valid, you should put it out by reducing the water with its value. 
Putting out fire also takes effort, and you need to calculate it. 
Its value is **equal to 25%** of the cell's value. 
In the end, you will have to **print the total effort**. 
**Keep** putting out cells until you run out of water. 
**Skip** it and try the next one if you do not have enough water to put out a given cell. In the end, print the cells you have put out in the following format:</br>
"Cells:
 - {cell1}
 - {cell2}
 …
 - {cellN}"</br>
"Effort: {effort}"</br>
The effort should be **formatted to the second decimal** place. 
In the end, print the **total fire** you have put out from all the cells in the following format:</br> 
**"Total Fire: {total_fire}"**</br>

**Input / Constraints**</br>
•	On the **1st line**, you will receive the fires with their cells in the format described above – integer numbers in the range [1…500].
•	On the **2nd line**, you will receive the water – an integer number in the range [0….100000].

**Output**</br>
Print the output as described above.

| Input                                                                   | Output |
|-------------------------------------------------------------------------|--------|
| High = 89#Low = 28#Medium = 77#Low = 23</br>1250                        |Cells:</br> - 89</br> - 28</br> - 77</br> - 23</br>Effort: 54.25</br>Total Fire: 217</br>|
| High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77</br>220 |Cells:</br> - 40</br> - 110</br>Effort: 37.50</br>Total Fire: 150</br>|

**Comments**: 
After reading the output, we start **checking** the **level of the fire** and its validity. 
The first is valid, so we **subtract the 89** from the amount of **water** – 1250, 
and the water becomes **1161**. 
We need to calculate the **effort**, which **is 25% of 89**. 
We will **add 89 to the total fire** we have put out. 
In the end, the **effort** is 54.22 and the **total fire**: 217

***Code***


    fire_input = input().split("#")
    water = int(input())
    total_fire, effort = 0, 0
    
    print("Cells:")
    for element in fire_input:
        element_value = int(element.split("= ")[1])
        if water >= element_value:
            if element.startswith("High") and element_value in range(81, 126):
                water -= element_value
                total_fire += element_value
                print(f" - {element_value}")
    
            elif element.startswith("Medium") and element_value in range(51, 81):
                water -= element_value
                total_fire += element_value
                print(f" - {element_value}")
    
            elif element.startswith("Low") and element_value in range(1, 51):
                water -= element_value
                total_fire += element_value
                print(f" - {element_value}")
    
    
        effort = total_fire * 0.25
    
    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {total_fire}")


**or** from Ivan Shopov


    cells = input().split("#")
    amount_of_water = int(input())
    total_fire = 0
    total_effort = 0
    fire_out_cells = []
    high = range(81, 125 + 1)
    medium = range(51, 80 + 1)
    low = range(1, 50 + 1)
    for cell in cells:
        type_of_fire, cell_value = cell.split(" = ")
        cell_value = int(cell_value)
        cell_is_valid = False
        if type_of_fire == "High":
            if cell_value in high:
                cell_is_valid = True
        elif type_of_fire == "Medium":
            if cell_value in medium:
                cell_is_valid = True
        elif type_of_fire == "Low":
            if cell_value in low:
                cell_is_valid = True
        if cell_is_valid: #cell is valid == True
            if amount_of_water >= cell_value:
                amount_of_water -= cell_value
                fire_out_cells.append(cell_value)
                total_effort += cell_value * 0.25
                total_fire += cell_value
    print("Cells:")
    for fire_cell in fire_out_cells:
        print(f" - {fire_cell}")
    print(f"Effort: {total_effort:.2f}")
    print(f"Total Fire: {total_fire}")


**or** from CEO


    fire_levels = input().split("#")
    water = int(input())
    
    put_out_cells = list()
    effort, total_fire, water_left = 0, 0, water
    
    for clean_text in fire_levels:
        type_of_fire, cell_value = [int(x) if x.isdigit() else x for x in clean_text.split(" = ")]
        if water_left >= cell_value:
            if any(["High" in type_of_fire and cell_value in range(81, 126),
                    "Low" in type_of_fire and cell_value in range(1, 51),
                    "Medium" in type_of_fire and cell_value in range(51, 81)]):
                put_out_cells.append(cell_value)
                effort += cell_value * 0.25
                total_fire += cell_value
                water_left -= cell_value
    
    print("Cells:")
    for n in put_out_cells:
        print(f" - {n}")
    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {total_fire}")

**or** from kumchovylcho


    fire_with_cells = input().split("#")
    current_water = int(input())
    putted_out_fire_cells = []
    effort = 0
    for cell in fire_with_cells:
        is_valid = False
        list_with_cells = cell.split()
        water_needed = int(list_with_cells[2])
        if current_water >= water_needed:
            if "High" in list_with_cells and water_needed in range(81, 126) or \
             "Medium" in list_with_cells and water_needed in range(51, 81) or \
             "Low" in list_with_cells and water_needed in range(1, 51):
                is_valid = True
        if is_valid:
            putted_out_fire_cells.append(water_needed)
            effort += water_needed * 0.25
            current_water -= water_needed
    
    print("Cells:")
    for cell in putted_out_fire_cells:
        print(f" - {cell}")
    print(f"Effort: {effort:.2f}\nTotal Fire: {sum(putted_out_fire_cells)}")


**or**


    fire_input = input().split("#")
    water = int(input())
    total_fire, effort = 0, 0
    
    print("Cells:")
    for element in fire_input:
        element_value = int(element.split("= ")[1])
    
        if water >= element_value and any(element.startswith(fire_type)
                                          and min_range <= element_value <= max_range
                                          for fire_type, min_range, max_range
                                          in [("High", 81, 125), ("Medium", 51, 80), ("Low", 1, 50)]):
            water -= element_value
            total_fire += element_value
            print(f" - {element_value}")
    
    effort = total_fire * 0.25
    
    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {total_fire}")


![](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/11_12_Lists%20Basics/12_Lists%20Basics%20-%20Exercise/09_hello_france.py)
