# Demonstrates defining a function without parameters


def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

"""or"""

# Demonstrates defining a function with a parameter

def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)


"""hello, world"""
# Demonstrates defining a function with a parameter with a default value

def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)

"""END"""

# Demonstrates defining a main function

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

""" """
