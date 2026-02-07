# INPUT

x = input("Enter your name: ")
print("Hello", x)

"""
NOTE: input() always returns a string.
"""

age = int(input("Enter your age: "))
print("You are", age, "years old")

"""
NOTE: We can use int(), float(), str() to convert the input to the desired type.
"""

name, age = input("Enter your name and age: ").split()
print("Name:", name)
print("Age:", age)

"""
NOTE: We can use split() to split the input into multiple values.
"""

name, age = input("Enter your name and age: ").split()
print("Name:", name)
print("Age:", age)

"""
NOTE: We can use try-except blocks to handle potential errors.
"""

try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
    
"""
 LIKE THIS :  there are other ways to get input from the user.
"""

# Using sys.stdin.readline()
# import sys
# name = sys.stdin.readline().strip()
# print("Hello", name)

# Using file input
# with open("input.txt", "r") as f:
#     name = f.readline().strip()
#     print("Hello", name)

# Using command-line arguments
# import sys
# name = sys.argv[1]
# print("Hello", name)