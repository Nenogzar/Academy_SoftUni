# Exercie: Lists Basics

[judge](https://judge.softuni.org/Contests/1725)


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


or


    lst = numbers.split(' ')
    new_list = list()
    for number in lst:
    
        if number[0] == "-":
            new_list.append(abs((int(number))))
        else:
            new_number = int(str("-" + number))
            new_list.append(new_number)
    
    print(new_list)

or

    invert_list = [-int(x) for x in input().split()]
    print(invert_list)

or

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


Code


    numner_one = int(input())
    numner_two = int(input())
    
    print_text = list()
    
    for number in range(1, numner_two + 1):
        print_text.append(number * numner_one)


or


    x = int(input())
    y = int(input())
    new_list=[]
    for n in range(x, x*y+1, x):
        new_list.append(n)


or 


    x, y = int(input()), int(input())
    new_list = [n for n in range(x, x*y+1, x)]
    print(new_list)


or 


    numner_one = int(input())
    numner_two = int(input())
    
    print([x * numner_one for x in range(1, numner_two + 1)])


3. Football Cards</br>
Most football fans love it for the goals and excitement. </br>
Well, this problem does not. You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
The rules:</br>

   *  **Two teams**, named "A" and "B" have 11 players each. </br>
   * **The players** on each team are numbered from 1 to 11. </br>
   * Any player may be sent off the field by being given a **red card**. </br>
   * If one of the teams has less than 7 players remaining, the referee stops the game immediately, and the team with less than 7 players loses.</br></br>
   The card is a string with the team's letter **("A" or "B")** followed by a single dash and the player's number. e.g., 
   the card **"B-7"** means player #7 from team B received a card.</br>
   
The task: You will be given a sequence of cards (could be empty), separated by a single space. 
You should print the count of remaining players on each team at the end of the game in the format: 
**"Team A - {players_count}; Team B - {players_count}"**. </br>
If the referee terminated the game, print an additional line: **"Game was terminated".**
   Note for the random tests: If a player who has already been sent off receives another card - ignore it.

Example

| Input | Otput | Input | Output                                      |
|-------|-------|-------|---------------------------------------------|
|A-1 A-5 A-10 B-2|Team A - 8; Team B - 10|A-1 A-5 A-10 B-2 A-10 A-7 A-3| Team A - 6; Team B - 10 Game was terminated |


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


or


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

