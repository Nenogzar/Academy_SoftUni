"""
https://judge.softuni.org/Contests/Practice/Index/4081#0

01. Temple of Doom

Harry will have to discover an important artifact in a cursed temple. Relying on the inscriptions at the entrance, 
Harry realizes that he will have to face unprecedented challenges. He must take all the useful things that he has in his truck...
There will be given two sequences of integers, representing tools and substances that he has at his disposal. 
There will also be a third sequence of integers, representing all challenges in the temple.
Your task is to take the first tool from the tools sequence and the last substance from the substances sequence. Multiply the values and check the result.
•	If the calculated result is equal to any of the elements from the challenges sequence, the challenge is resolved. 
You need to remove both the tool and the substance from their sequences. The challenge should also be removed from its sequence.
  •	If the calculated result is not equal to any of the elements from the challenges sequence, the challenge is not resolved:
    o	Increase the value of the tool element by 1 and move the element to the back of the tools’ sequence.
    o	Decrease the value of the substance element by 1 and return the element to the substance’s sequence. If the value of the substance element reaches 0, remove it from the sequence.
If Harry has no substances or tools left (the substances sequence is empty) but has more challenges to resolve, 
he is lost in the temple forever. End the program and print on the console the following message:
  •	"Harry is lost in the temple. Oblivion awaits him."
If Harry manages to pass all the challenges, he will find the artifact. End the program and print on the console the following message:
  •	"Harry found an ostracon, which is dated to the 6th century BCE."
Input
  •	The first line will represent the tools that Harry has at his disposal – integers, separated by a single space.
  •	The second line will represent the substances that Harry has at his disposal – integers, separated by a single space.
  •	The third line will represent the challenges that Harry will have to resolve – integers, separated by a single space.
Output
  •	On the first line print on the console the appropriate message, among the following:
    o	"Harry is lost in the temple. Oblivion awaits him."
    o	"Harry found an ostracon, which is dated to the 6th century BCE."
  •	On the next three lines, print on the console the elements of the non-empty sequences, in the following format:
    o	"Tools: element1, element2, element3 … elementn"
    o	"Substances: element1, element2, element3 … elementn"
    o	"Challenges: element1, element2, element3 … elementn"
Constraints
  •	All the given numbers will be valid integers in the range [1, 100].
  •	There will be no negative inputs.
Examples

Input
2 4 6 8
11 3 5 7 9
24 28 18 30


Output
Harry found an ostracon, which is dated to the 6th century BCE.
Substances: 11

Input
13 7 4 22 11 15 20
3 2 1
12 10 5

Output
Harry is lost in the temple. Oblivion awaits him.
Tools: 20, 14, 8, 5, 23, 12, 16
Challenges: 12, 10, 5


"""

##########: variant 1 :##########

from collections import deque

tools_que = deque([int(t) for t in input().split()])
substances_stack = [int(s) for s in input().split()]
challenges = [int(c) for c in input().split()]

while challenges and substances_stack:
    current_tool = tools_que.popleft()
    current_substance = substances_stack[-1]
    current_product = current_tool * current_substance
    if current_product in challenges:
        challenges.remove(current_product)
        substances_stack.pop()
        continue
    current_tool += 1
    tools_que.append(current_tool)
    substances_stack[-1] -= 1
    if substances_stack[-1] == 0:
        substances_stack.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools_que:
    print(f"Tools: {', '.join([str(t) for t in tools_que])}")
if substances_stack:
    print(f"Substances: {', '.join([str(s) for s in substances_stack])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")

##########: variant 2 :##########

