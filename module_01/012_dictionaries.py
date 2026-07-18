# Dictionaries are used to store data values in key:value pairs. They are non-ordered, changeable, and do not allow duplicates.

# 1. Creating a dictionary
person = {
  "name": "Fernando", 
  "age": 100,
  "city": "Luanda"
  }

# showing the dictionary
print("My dictionary:", person)


# accessing elements by key
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])  


# adding a new key-value pair to the dictionary after creation
person["country"] = "Angola"
print("My dictionary after adding country:", person)


# exception "key error" occurs when the key is not found in the dictionary. To avoid this, we can use the get() method which returns None if the key is not found.
print("Country:", person.get("country"))  # returns None since "country" key is not found in the dictionary.

