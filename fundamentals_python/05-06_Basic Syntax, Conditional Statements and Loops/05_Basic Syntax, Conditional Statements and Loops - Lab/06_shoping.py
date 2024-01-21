""" 1 """
# budget = int(input())
# total = 0
# while True:
#     command = input()
#
#     if command == "End":
#         print("You bought everything needed.")
#         break
#     current_price = int(command)
#     budget -= current_price
#     if budget <= 0:
#         print("You went in overdraft!")
#         break

""" 2 """
# budget = int(input())
# command = input()
#
# while command != "End":
#     expense = int(command)
#     budget -= expense
#
#     if budget < 0:
#         print("You went in overdraft!")
#         break
#     command = input()
# else:
#     print("You bought everything needed.")

""" 3 
This code uses iter(input, "End"), which creates an iterator that terminates when "End" is entered. 
This avoids the need for a separate line that initializes command before entering the loop. 
Also, this code moves the check for "End" into the loop itself
"""
# budget = int(input())
#
# for command in iter(input, "End"):
#     expense = int(command)
#     budget -= expense
#
#     if budget < 0:
#         print("You went in overdraft!")
#         break
# else:
#     print("You bought everything needed.")
