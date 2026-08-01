"""
Let's explore what multiple inheritance is and how we can use it in our programs.
We'll start by creating a file named "herança-múltipla.py". 
Next, I'll show an example of standard inheritance, where we create an "animal" class with methods and attributes common to all animals. 
Then, we'll create child classes to inherit these methods and attributes. For instance, we'll create a "mammal" class that inherits from "animal" and includes the ability to nurse. 
We'll also create a "bird" class that inherits from "animal" and includes a "fly" method. After that, I'll demonstrate multiple inheritance by creating a "bat" class that inherits from both "mammal" and "bird". 
To implement multiple inheritance, we use a comma to separate the classes being inherited from. I'll also show how to implement methods specific to the "bat" class using the "super" function. Finally, we'll run some tests to verify that everything is working correctly. 
Multiple inheritance allows us to inherit from several different classes and access all their methods and attributes.
"""

class Animal:
  def __init__(self, name):
      self.name = name

  def emit_sound(self):
     pass


class Mammal(Animal):
   def breastfeed(self):
      return f"{self.name} is breastfeeding."

class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying."

class Bat(Mammal, Bird):
    def emit_sound(self):
        return f"{self.name} is emitting a sound."


bat = Bat("Batman")

# Accessing base class Animal methods
print("Bat name:", bat.name)
print("Bat sound:", bat.emit_sound())

# Accessing Mammal and Bird methods
print("Bat is breastfeeding: ", bat.breastfeed())
print("Bat is flying: ", bat.fly())
