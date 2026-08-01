"""
Pillars of Object-Oriented Programming: abstraction, encapsulation, inheritance, and polymorphism.
These concepts are key strategies for managing classes and effectively utilizing the Object-Oriented Programming paradigm.
Let's start with inheritance, one of the most important pillars. Through inheritance, we can create classes that inherit attributes and methods from a parent class.
I’ll provide an example using an `Animal` class, where we can create subclasses like `Dog` and `Cat`; these inherit attributes and methods from the `Animal` class but can also exhibit specific behaviors, such as making different sounds. 
We will also discuss polymorphism, which allows us to use the same method in different ways across various derived classes. Polymorphism is widely used in Object-Oriented Programming.

"""

# Inheritance
print("\nExample of Inheritance")

class Animal:
  def __init__(self, name) -> None:
    self.name = name


  def walk(self):
    return print(f"O animal {self.name} walked.")

  def emit_sound(self):
    pass

class Dog(Animal):
  def emit_sound(self):
    return "Au, au"


class Cat(Animal):
  def emit_sound(self):
    return "Miauu!!!"