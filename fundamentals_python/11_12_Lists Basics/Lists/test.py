""" You guessed it! Buzzzz """
play = False
print("What is my favourite food?")
while play == False:
  guess = input("Guess? ")
  if guess == "electricity":
    print ("You guessed it! Buzzzz")
    play = True
  else:
    print("Not even close.")

""" Cheer """
cheer = input("Cheer: ")
numb = 0
while numb<len(cheer):
  print(f"Give me a {cheer[numb]}, {cheer[numb]}!")
  numb = numb+1
print("What does it spell?")
print(cheer.upper())


""" Steps """
# __
#   |_
#     |_
#       |_
#         |_
# __________|

steps = int(input("How many steps? "))
print("__")
spaces = ("  ")
for i in range(steps-1):
  print(f"{spaces}|_")
  spaces = spaces.join("  ")
print("__"*steps+"|")


""" """

expenses = input("Enter the expenses: ")
expenses = expenses.split()
amount = 0
for i in range(len(expenses)):
  amount = amount + int(expenses[i])
print (f"Total: ${amount}")



