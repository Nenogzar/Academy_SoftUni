# Step 1: Read user input for the number and position
number = int(input())
p = int(input())

# Step 2: Shift the number 7 (binary: 111) p times to the left to create the mask
mask = 7 << p

# Step 3: Invert the values of the three bits starting from position p using XOR
result = number ^ mask

# Print the resulting integer
print(f"The resulting integer after inverting 3 bits from position {p} is: {result}")
