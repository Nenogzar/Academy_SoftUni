# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# •	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# •	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."
"""""""""
+------------------------------------+
|       INPUT                        |
+------------------------------------+
2
Here is a name @George| and an age #18*
Another name @Billy| #35* is his age
+------------------------------------+
+    OUTPUT                          |
+------------------------------------+
George is 18 years old. 
Billy is 35 years old.
+------------------------------------+
|       INPUT                        |
+------------------------------------+
3
random name @lilly| random digits #5*age
@Marry| with age #19*
here Comes @Garry|he is #48* years old
+------------------------------------+
+    OUTPUT                          |
+------------------------------------+
lilly is 5 years old.
Marry is 19 years old.
Garry is 48 years old.

"""""""""
#########################################*-*line.find()*-*##########################################

# n = int(input())
#
# for _ in range(n):
#     line = input()
#
#     name_start = line.find('@')
#     name_end = line.find('|', name_start)
#
#     age_start = line.find('#', name_end)
#     age_end = line.find('*', age_start)
#
#     if name_start != -1 and name_end != -1 and age_start != -1 and age_end != -1:
#         name = line[name_start + 1:name_end]
#         age = line[age_start + 1:age_end]
#         print(f"{name} is {age} years old.")

#########################################*-*line.index()*-*##########################################
n = int(input())

for _ in range(n):
    line = input()

    name_start = line.index('@')
    name_end = line.index('|', name_start)

    age_start = line.index('#', name_end)
    age_end = line.index('*', age_start)

    if name_start != -1 and name_end != -1 and age_start != -1 and age_end != -1:
        name = line[name_start + 1:name_end]
        age = line[age_start + 1:age_end]
        print(f"{name} is {age} years old.")





##########################################*-*FROM*Tamer*-*##########################################

number1 = int(input())
name_tamer = ''
age_tamer = ''
for _ in range(number1):
    text = input()


    name_start_idx = text.index('@')
    name_final_idx = text.index('|')
    name_tamer = text[name_start_idx + 1: name_final_idx]

    age_start_idx = text.index('#')
    age_final_idx = text.index('*')
    age_tamer = text[age_start_idx + 1: age_final_idx]

    print(f'{name_tamer} is {age_tamer} years old.')

###################################*-*NEXT*LEVEL***FROM*Tamer*-*####################################

number2 = int(input())
for _ in range(number2):
    texta = input()

    get_symbol_index = lambda text_line, symbol: text_line.index(symbol)
    get_result = lambda name_starta, name_enda, age_starta, age_enda: f"{texta[name_starta + 1:name_enda]} is {texta[age_starta + 1:age_enda]} years old."

    print(
        get_result(get_symbol_index(texta, "@"),
                   get_symbol_index(texta, "|"),
                   get_symbol_index(texta, "#"),
                   get_symbol_index(texta, "*")
                   )
    )

####################################*-*NEXT*LEVEL***FROM*CEO*-*#####################################

number_strings = int(input())

for _ in range(number_strings):
    test_string = input()
    name_ceo = test_string[test_string.index("@") + 1:test_string.index("|")]
    age_ceo = test_string[test_string.index("#") + 1:test_string.index("*")]
    print(f"{name_ceo} is {age_ceo} years old.")

