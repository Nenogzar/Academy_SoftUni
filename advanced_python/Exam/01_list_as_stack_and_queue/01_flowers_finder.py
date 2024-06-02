# ******* Advanced Exam - 19 February 2022 ******* #

# *******  01_flowers_finder  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3374#0

You will be given two sequences of characters, representing vowels and consonants.
    Your task is to start checking if the following words could be found:

•	"rose"
•	"tulip"
•	"lotus"
•	"daffodil"

Start by taking the first character of the vowels collection and the last character from the consonants collection.
Then check if these letters are present in one or more of the given words.
If a letter is present, that part of the word is considered found.
The word is gradually revealed with each letter found.
Continue processing the next couple of letters until you find one of the given words above.

A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:

•	The letter "o" is present in "rose", "lotus", and "daffodil".
•	The letter "l" is present in "tulip", "lotus", and "daffodil".
•	The letter "f" is present in the word "daffodil" twice.

The consonant and the vowel are always removed from the collection
    after trying to match them with the letters in the given words (whether successful or not).
In the end, the program stops when a word is found, or there are no more vowels or consonants.
As a result, if you found a word, print it and the remaining letters in each collection in the format described below.
Otherwise, print
    "Cannot find any word!"
    on the first line and the remaining letters in each sequence in the format described below.

Look at the provided examples for a better understanding of the problem.

Input
•	On the first line, you will receive vowels, separated by a single space (" ").
•	On the second line, you will receive consonants, separated by a single space (" ").

Output
•	On the first line:
    o	If a word is found, print it in the format:
        "Word found: {word_found}"
    o	Otherwise, print:
        "Cannot find any word!"

•	On the next lines, print the remaining letters in each collection (if there are any left):
    "Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
    "Consonants left: {consonants_one} {consonants_two} … {consonants_N}"

Constraints
•	All letters will be lowercase.
•	The letter 'y' will always be a vowel.
•	The letter 'w' will always be a consonant.

Input
o e a o e a i
p r s x r

Output
Word found: rose
Vowels left: o e a i
Consonants left: p r


*** Comment ***
Start by taking the first volew "o" and the last consonant "r". They are found in words "rose", "lotus", and "daffodil".
Then, take "e" and "x". They are found in thr word "rose".
Then, take "a" and "s". They are found in words "rose", "lotus", and "daffodil".
The word "rose" is found, so we print it. Then we print the remaining letters in each sequence.

Input
a a a
x r l t p p

Output
Cannot find any word!
Consonants left: x r l

Input
u a o i u y o e
p m t l

Output
Word found: tulip
Vowels left: u y o e

"""

##########: variant 1 whit set() in dict :##########

from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = ["rose", "tulip", "lotus", "daffodil"]

# събиране на намерините букви във всяка дума
found_letters = {word: set() for word in words}

word_found = False
found_word = ""

while vowels and consonants and not word_found:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    # проверка на двата знака във всяка дума
    for word in words:
        if vowel in word:
            found_letters[word].add(vowel)
        if consonant in word:
            found_letters[word].add(consonant)

        # Думата напълно намерена ли е ?
        if set(word) == found_letters[word]:
            found_word = word
            word_found = True
            break

if word_found:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")


##########: variant 2   whit Dictionary :##########


from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

find_flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

found_flower = None

while vowels and consonants and not found_flower:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key, flower in find_flowers.items():
        if current_vowel in flower:
            find_flowers[key] = find_flowers[key].replace(current_vowel, "")
        if current_consonant in flower:
            find_flowers[key] = find_flowers[key].replace(current_consonant, "")
        if not find_flowers[key]:
            found_flower = key
            del find_flowers[key]
            break

if found_flower:
    print(f"Word found: {found_flower}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")



##########: variant 3 solution SoftUni :##########

from collections import deque


def check_word(char, word):
    if char in word:
        word = word.replace(char, "")
    return word


flowers = ["rose", "tulip", "lotus", "daffodil"]
found_word = False

vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for index in range(len(flowers)):
        flowers[index] = check_word(vowel, flowers[index])
        if flowers[index] == '':
            found_word = True
            break
        flowers[index] = check_word(consonant, flowers[index])
        if flowers[index] == '':
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
else:
    found_index = flowers.index("")
    if found_index == 0:
        print("Word found: rose")
    elif found_index == 1:
        print("Word found: tulip")
    elif found_index == 2:
        print("Word found: lotus")
    elif found_index == 3:
        print("Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

##########: variant 4 solution SoftUni :##########

from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    for word in words.keys():
        words[word] = words[word].replace(v, '')
        words[word] = words[word].replace(c, '')
        if words[word] == '':
            print(f"Word found: {word}")
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

