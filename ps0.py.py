import numpy as np

print("Problem Set")
print("MIT 60001: Introduction to Computer Science and Programming in Python")
print("My name is Bhuti")
print("My birthday is 06/20/1976")

# Ask the user to enter a number 'x'
x = float(input("Enter a number x: "))
# Ask the user to enter a number 'y'
y = float(input("Enter a number y: "))
# Prints out number 'x' raised to the power 'y'
print(f"{x} raised to the power {y} is {x**y}")
# Prints out the log (base 2) of 'x'
print(f"log base 2 of {x} is {np.log2(x)}") 