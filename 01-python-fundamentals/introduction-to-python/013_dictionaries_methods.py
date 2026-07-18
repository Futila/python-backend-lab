# How to update a dictionary property by assigning a new value to an existing key in the dictionary.
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Person before update:", person)

# Update the age property
person["age"] = 31

print("Person after update:", person)


# removing a property from a dictionary using the del statement.
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
} 

print("Person before deletion:", person)

# Remove the city property
del person["city"] 

print("Person after deletion:", person)


# ======================================================#

# 3 main methods of dictionaries in Python are:

# 1. keys() - returns a view object that displays a list of all the keys in the dictionary.
# 2. values() - returns a view object that displays a list of all the values in the dictionary.
# 3. items() - returns a view object that displays a list of a dictionary's key-value tuple pairs.


print("Dictionary methods demonstration:")
keys = list(person.keys())
values = person.values()
items = person.items()

print("Keys:", keys)
print("First key:", keys[0])  # Accessing the first key


print("Values:", values)
print("First value:", list(values)[0])  # Accessing the first value


print("Items:", items)
print("First item:", list(items)[0])  # Accessing the first item (key-value pair)


print("Accessing second item's key:", list(items)[1][0])
print("Accessing second item's value:", list(items)[1][1])