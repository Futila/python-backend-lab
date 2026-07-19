# Exceptions are errors that occur during the execution of a program. 
# In Python, exceptions can be handled using try and except blocks. 
# Here's an example of how to handle exceptions in Python:


while True:
  try:
    print("Welcome to the exception handling example!")
    number = int(input("Please enter an integer number: "))
    result = 10 / int(number)  # This line may raise a ValueError or ZeroDivisionError
   

  except ValueError as e: 
    print(f"Invalid input! Please enter a valid integer number. Error of ValueError: {e}")
    raise ValueError("Incorrect input type. Please enter an integer.") 
  
  except Exception as e:
    print(f"An error occurred: {e}")

  else: # will execute if no exception occurs
    print("No exceptions occurred. The program executed successfully.")
    print(f"The result of 10 divided by {number} is: {result}")
    break  # Exit the loop if everything went well

  finally: # will always execute, regardless of whether an exception occurred or not
    print("This block will always execute, regardless of whether an exception occurred or not.")
    print("Operation finalized.")

