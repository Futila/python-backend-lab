# Loop is as a control flow statement that allows code to be executed repeatedly based on a given condition. The most common types of loops are "for" loops and "while" loops.

# For loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.

# List
list = [1, 3, 4, 5,6, 7, 8, 9, 10]
for element in list:
  print(element)


# Tuple
tuple = (1, 2, 3, 4, 5)
for element in tuple:
  print(element)


# Dictionary

person = {
  "name": "Fernando", 
  "age": 40, 
  "city": "Luanda"
}

print("For using dictionary - keys")
for key in person.keys():
  print(key)



print("\nFor using dictionary - values")
for value in person.values():
  print(value)



print("\nFor using dictionary - items")
for key, value in person.items():
  print(f"{key}: {value}")



students = ["Fernando", "Mendes", "Natalia", "Carolina", "Margarida"]

for student in students:
  print(f"hello {student}, welcome to computer engineer course at Federal University of Santa Catarina")


