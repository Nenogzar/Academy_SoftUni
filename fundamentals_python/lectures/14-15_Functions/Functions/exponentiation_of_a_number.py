# Степенуване на число
def main():
    x = int(input("What's x? "))
    print("x grading is: ", grading(x))

def grading(n):
    y = int(input("to what degree? "))
    return pow(n, y)

main()
