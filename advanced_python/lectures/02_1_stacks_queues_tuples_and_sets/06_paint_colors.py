#################################### TASK CONDITION ############################
"""

                        6.	Paint Colors
You will have to find all possible color combinations that can be used.
Write a program that finds colors in a string. You will be given a string on a 
single line containing substrings (separated by a single space) from which 
you will be able to form the following colors: 
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings 
and check if you can get any of the above colors' names. If there is only
one substring left, you should use it to do the same check. You can only keep 
a secondary color if the two main colors needed for its creation could be 
formed from the given substrings:
•	orange = red + yellow
•	purple = red + blue
•	green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary 
color after it is found. When you form a color, remove both substrings. 
Otherwise, you should remove the last character of each substring and return 
them in the middle of the original string. If the string contains an odd 
number of substrings, you should put the substrings one position ahead. For example,
if you are given the string "re yellow bye" you could not form a color with 
the substring "re" and "bye", so you should remove the last character and return 
them in the middle of the string: "r by yellow". In the end, print out the 
list with colors in the order in which they are found.
Input
•	Single line string
Output
•	The list with the collected colors
Constrains
•	You will not receive an empty string
•	Please consider only the colors mentioned above
•	There won't be any cases with repeating colors

____________________________________________________________________________________________
Example_01

Input
d yel blu e low redd	

Output
['yellow', 'blue', 'red']

Explanation
First, we take "d" and "redd". After combining those substrings, we don't get 
any of the needed colors, so we remove the last characters from both substrings 
and return them in the middle of the original string, and it becomes "yel blu red e low".
After that, we take "yel" and "low" so the first color we add to our list is 
yellow, and the string we are searching in looks as follows: "blu red e"
Then we take "blu" and "e", and since this color is one of the searched ones 
(blue), we add it to our collection, and the state of the string is now "red".
We should take the last substring and check if it matches some of the colors, 
and since it does, we add it (red) to our colors collection.
Finally, we print all the colors found: yellow, blue, and red in the format shown above.

____________________________________________________________________________________________
Example_02

Input
r ue nge ora bl ed	

Output
['red', 'blue']

Explanation
We don't keep orange because we don't have yellow in the final 
list with colors (combining red and yellow gives us orange).

____________________________________________________________________________________________
Example_03

Input
re ple blu pop e pur d	

Output
['red', 'purple', 'blue']


"""
##########: variant 1 :##########

from collections import deque

string_with_substrings = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
final_list = []

while string_with_substrings:
    if len(string_with_substrings) > 1:
        first_color = string_with_substrings.popleft()
        last_color = string_with_substrings.pop()
    else:
        first_color = string_with_substrings.popleft()
        last_color = ""

    first_way = first_color + last_color
    second_way = last_color + first_color
    if first_way in main_colors or first_way in secondary_colors:
        final_list.append(first_way)
    elif second_way in main_colors or second_way in secondary_colors:
        final_list.append(second_way)
    else:
        first_color = first_color[:-1]
        last_color = last_color[:-1]
        if first_color:
            string_with_substrings.insert(len(string_with_substrings) // 2, first_color)
        if last_color:
            string_with_substrings.insert(len(string_with_substrings) // 2, last_color)

required_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for color in final_list.copy():
    if color in secondary_colors:
        required_primary_colors = required_colors[color]
        if not all(primary_color in final_list for primary_color in required_primary_colors):
            final_list.remove(color)

print(final_list)


##########: variant 2 :##########
from collections import deque


class PaintColors:

    def __init__(self):
        self.result_output_message = []
        self.initial_string = deque()
        self.collected_colors = []
        self.color_pairs = {'orange': ('red', 'yellow'),
                            'purple': ('red', 'blue'),
                            'green': ('yellow', 'blue'),
                            }
        self.main_meth()

    def main_meth(self):
        self.define_initial_string_as_deque()
        self.start_to_matching_colors()
        self.check_primary_colors_to_form_secondary_colors()

    def define_initial_string_as_deque(self):
        self.initial_string = deque(input().split())

    def start_to_matching_colors(self):
        while self.initial_string:
            first = self.initial_string.popleft()
            second = self.initial_string.pop() if self.initial_string else ''

            variant01, variant02 = first + second, second + first
            color = self.check_variants_for_match_color(variant01, variant02)

            if color:
                self.collected_colors.append(color)
            else:
                self.return_substring_to_initial_string(first, second)

    def check_variants_for_match_color(self, combination01, combination02):
        for secondary, main in self.color_pairs.items():
            if combination01 == secondary or combination01 in main:
                return combination01
            elif combination02 == secondary or combination02 in main:
                return combination02

    def return_substring_to_initial_string(self, first, second):
        first_edit, second_edit = first[:-1], second[:-1]
        middle = len(self.initial_string) // 2
        if first_edit:
            self.initial_string.insert(middle, first_edit)
        if second_edit:
            self.initial_string.insert(middle, second_edit)

    def check_primary_colors_to_form_secondary_colors(self):
        founded_secondary_colors = set(self.color_pairs).intersection(self.collected_colors)

        for color in founded_secondary_colors:
            if not set(self.color_pairs[color]).issubset(self.collected_colors):
                self.collected_colors.remove(color)

    def __repr__(self):
        return f'{self.collected_colors}'


if __name__ == '__main__':
    print(PaintColors())


