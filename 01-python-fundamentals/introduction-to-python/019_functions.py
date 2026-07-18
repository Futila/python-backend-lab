# Functions

# A function in python is a block of code that can be reused many times, and executes a specific task when called.


def greetings(name):
  print(f"Hello {name}")


print("Calling greetings function.")
greetings("Fernando")
greetings("Futila")



# Function with return
def square(number):
  result = number ** 2
  return result

print(square(2))

