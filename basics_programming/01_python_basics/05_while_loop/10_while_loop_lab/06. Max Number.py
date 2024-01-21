max_number = float("-inf")  # Initialize max_number to negative infinity

while True:
    user_input = input()

    if user_input == "Stop":
        break

    #try:
    number = int(user_input)
    max_number = max(max_number, number)
   # except ValueError:
        # print("Invalid input. Please enter an integer or 'Stop'.")

#if max_number != float("-inf"):
print(max_number)
#else:
    #print("No valid numbers were entered.")
