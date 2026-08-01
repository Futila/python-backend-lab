"""
`class method` and `static method`. A `class method` is used to create instances based on global configurations, whereas a `static method` is used to execute specific functions without accessing instance or class attributes. 
It is important to be cautious when using too many static methods, as this can make the code confusing and difficult to maintain later on. Let's learn how to use these decorators to improve our object-oriented programming.
"""

# @classmethod
# @staticmethod


class MyClass:
  value = 10 # class attribute

  def __init__(self, name) -> None:
      self.name = name # instance attribute

  # requires an instance to be called
  def instance_method(self):
    return f"Instance method called for {self.name}"

  # receives class reference
  @classmethod
  def class_method(cls):
    return f"Class method called for {cls.value}"

  # Does not receive any argument, but can execute an specific function
  @staticmethod
  def static_method():
    return "Static method called"
  
     

obj = MyClass(name="Example Class")
print(obj.instance_method())
print(MyClass.value)
print(MyClass.class_method())
print(MyClass.static_method())


#

class Car:
  def __init__(self, brand, model, year) -> None:
    self.brand = brand
    self.model = model
    self.year = year


  @classmethod

  #cls is the class Car
  def create_car(cls, configuration):
    brand, model, year = configuration.split(",")
    return cls(brand, model, int(year))


configuration1 = "Toyota,Corolla,2024"
car1 = Car.create_car(configuration1)
print(f"Brand: {car1.brand}\nModel: {car1.model}\nYear: {car1.year}")


class Mathematics:

  @staticmethod
  def sum(a,b):
    return a + b

print(Mathematics.sum(a=10, b=5))
