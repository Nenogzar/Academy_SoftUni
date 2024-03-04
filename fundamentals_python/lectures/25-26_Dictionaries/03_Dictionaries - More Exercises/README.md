<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">


<table>
  <tr>
    <th><a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries"><img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/image/13.jpg" alt="Dictionary" width="300"></a>
</th>
    <th>Legend:<br>Under each task name, you have two choices:<br>🛠️Condition - task conditions<br>🐍Code - solution of tasks</th>
  </tr>
  <tr>
    <td>
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/01_Dictionaries%20-%20Lab">Lab</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/02_Dictionaries%20-%20Exercise">Exercise</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/03_Dictionaries%20-%20More%20Exercises">More</a>
    </td>
    <th><a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/03_Dictionaries%20-%20More%20Exercises/Exercise">problem solving python files</a></th>
  </tr>

</table>


[judge](https://judge.softuni.org/Contests/Practice/Index/1738)
> ## Dictionaries - Exercise

<details><summary> TASK CONDITIONS 🛠️ AND SOLUTION OF TASKS 🐍</summary>


> 1. Ranking
<details><summary>🛠️Condition</summary>

Here comes the final and the most interesting part – the Final ranking of the candidate-interns. 
The final ranking is **determined** by the **points** of the interview tasks and by the points from the exams in SoftUni. 
Here is your final task. You will receive some lines of input in the format **"{contest}:{password for contest}"** 
until you receive **"end of contests"**. 
Save that data because you will need it later. 
After that you will receive another type of input in the format **"{contest}=>{password}=>{username}=>{points}"** 
until you receive "end of submissions". Here is what you need to do.

* Check if the contest is valid (It is considered valid if you received it in the first type of input)
* Check **if the password is correct** for the **given contest**
* If the **contest and the password are valid**, **save** the **user** with the contest they take part in 
(a user can take part in many contests) and the **points the user has in the given contest**. 

If you **receive** the same contest and the same user update the **points only if the new ones are more than the older ones**.

In the end, you should **print** the info for the user with the most points 
(total points for all contents they participated in) in the format **"Best candidate is {user} with total {total_points} points."**. 
After that print all students ordered by their names. 
For each user print each contest with the points in descending order. See the examples.

#### Input

* Strings in format **"{contest}:{password for contest}"** until the "end of contests" command. There will be no case with two equal contests
* Strings in format **"{contest}=>{password}=>{username}=>{points}"** until the **"end of submissions"** command.
* There will be no case with 2 or more users with the same total points!
#### Output
* On the first line, print the best user in the format **"Best candidate is {user} with total {total points} points."**.
* Then print all students ordered as mentioned above in the format:

**{user_name1}**
**# {contest1} -> {points}**
**# {contest2} -> {points}**
**…**
**# {contestN} -> {points}**

#### Constraints

* The strings may contain any ASCII character except from **(:, =, >)**.
* The numbers will be in range [0 - 10000].
* Second input is always valid.

Example

| Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Output                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Part One Interview:success<br>JS Fundamentals:fundExam<br>C# Fundamentals:fundPass<br>Algorithms:fun<br>end of contests<br>C# Fundamentals=>fundPass=>Tanya=>350<br>Algorithms=>fun=>Tanya=>380<br>Part One Interview=>success=>Nikola=>120<br>Java Basics Exam=>wrong_pass=>Teo=>400<br>Part One Interview=>success=>Tanya=>220<br>OOP Advanced=>password123=>Kay=>231<br>C# Fundamentals=>fundPass=>Tanya=>250<br>C# Fundamentals=>fundPass=>Nikola=>200<br>JS Fundamentals=>fundExam=>Tanya=>400<br>end of submissions | Best candidate is Tanya with total 1350 points.<br>Ranking:<br>Nikola<br># C# Fundamentals -> 200<br># Part One Interview -> 120<br>Tanya<br># JS Fundamentals -> 400<br># Algorithms -> 380<br># C# Fundamentals -> 350<br># Part One Interview -> 220                                    |
| Java Advanced:funpass<br>Part Two Interview:success<br>Math Concept:asdasd<br>Java Web Basics:forrF<br>end of contests<br>Math Concept=>ispass=>Monika=>290<br>Java Advanced=>funpass=>Simona=>400<br>Part Two Interview=>success=>Drago=>120<br>Java Advanced=>funpass=>Petyr=>90<br>Java Web Basics=>forrF=>Simona=>280<br>Part Two Interview=>success=>Petyr=>0<br>Math Concept=>asdasd=>Drago=>250<br>Part Two Interview=>success=>Simona=>200<br>end of submissions                                                  | Best candidate is Simona with total 880 points.<br>Ranking:<br>Drago<br># Math Concept -> 250<br># Part Two Interview -> 120<br>Petyr<br># Java Advanced -> 90<br># Part Two Interview -> 0<br>Simona<br># Java Advanced -> 400<br># Java Web Basics -> 280<br># Part Two Interview -> 200 |



</details>

<details> <summary>🐍Code</summary>


```Python
 

```

</details>





</details>