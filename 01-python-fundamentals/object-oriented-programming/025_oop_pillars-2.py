"""
three fundamental concepts: inheritance, polymorphism, and encapsulation. First, we explored how to create classes that inherit attributes and methods from other classes. 
Next, we looked at using polymorphism to implement different behaviors for common methods across different classes. 
Finally, we covered encapsulation, which involves using private attributes and methods to protect sensitive information and ensure data integrity. 
We demonstrated how to create a bank account class with private attributes and methods for depositing, withdrawing, and checking the balance.
When testing the program, we saw how encapsulation constraints ensure data security.
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
