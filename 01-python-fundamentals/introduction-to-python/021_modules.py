# modules in python are files that contain python code. 
# They can define functions, classes, and variables that you can reuse in other python programs. 
# You can also use built-in modules that come with python or install third-party modules using package managers like pip.


import math  # importing the built-in math module
from math import sqrt  # importing only the sqrt function from the math module


square_root = sqrt(16) 

print(f"The square root of 16 is: {square_root}")


print("\nExample of a custom module")
import my_module

message = my_module.greeting("Alice")
print(message)

result_double = my_module.double(5)
print(f"Double of 5 is: {result_double}")