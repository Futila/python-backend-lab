"""
An abstract class cannot be instantiated directly but serves as a template for other classes. 
This helps us safeguard the characteristics—such as attributes and methods—that a class must possess. 
In Python, we can use the ABC module to create abstract classes. 
When creating a derived class, it is mandatory to implement the methods defined in the abstract class. 
This ensures code safety and consistency, even when working with different derived classes.


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

# emit_sound above has different implementations -> polymorphism
# Polymorphism

dog = Dog(name="Rex")
cat = Cat(name="Tely")

print("\nPolymorphism Example")
animals = [dog, cat]

for animal in animals:
  print(f"{animal.name} makes: {animal.emit_sound()}")


# Encapsulation - uses private attributes
class BankAccount:
  def __init__(self, balance) -> None:
    self.__balance = balance # Private attribute

  def deposit(self, value):
    if value > 0:
      self.__balance += value

  def withdraw(self, value):
    if value > 0 and value <=self.__balance:
      self.__balance -= value

  def check_balance(self):
    return self.__balance


account = BankAccount(balance=1000)
print(f"Bank Account balance: {account.check_balance()}")

account.deposit(value=500)
print(f"Bank Account balance: {account.check_balance()}")

account.deposit(value=-500)
print(f"Bank Account balance: {account.check_balance()}")

account.withdraw(value=200)
print(f"Bank Account balance: {account.check_balance()}")




# Abstraction
print("\nAbstraction Example")
from abc import ABC, abstractmethod

class Vehicle(ABC):

  @abstractmethod
  def turn_on(self):
    pass

  @abstractmethod
  def turn_off(self):
    pass


class Car(Vehicle):
  def __init__(self) -> None:
    pass

  def turn_on(self):
    return "Car turned on"

  def turn_off(self):
      return "Car turned off"

car = Car()
print(car.turn_on())
print(car.turn_off())