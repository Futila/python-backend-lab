"""
A decorator is a special type of function that allows you to modify or extend the behavior of other functions without altering their original code. 
You can add functionality both before and after the function is called. The syntax for creating a decorator involves defining a function that takes another function as an argument and returns a "wrapper" that encloses the original function. 
Decorators can be used to add validations—such as checking if a user is logged in. It is also possible to create a decorator as a class, where the function is assigned to a property and executed within the wrapper. 
Both approaches work in the same way, enabling you to modify function behavior without changing the internal code.

"""

# Decorator as function
def my_decorator(func):
  def wrapper():
    print("Before the function is called")
    func()
    print("After the function is called")
  return wrapper


@my_decorator
def my_function():
  print("My function was called.")


my_function()



# Decorator as class
class MyClassDecorator:
    def __init__(self, func) -> None:
     self.func = func

    def __call__(self) -> any:
        print("Before my function is called (class decorator)")
        self.func()
        print("After my function is called (class decorator)")


@MyClassDecorator
def second_function():
   print("Second function was called")


second_function()