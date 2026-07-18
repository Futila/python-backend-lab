# using funcion range() to generate a sequence of numbers and iterate over them using a for loop.
# The range() function generates a sequence of numbers, which can be used in for loops to iterate over a specific range of values.
#  The range() function can take one, two, or three arguments, depending on the desired range of numbers.

# Example 1: Using range() with one argument
print("Example 1: Using range() with one argument")
for i in range(5):  # Generates numbers from 0 to 4
    print(i)

# Example 2: Using range() with two arguments
print("\nExample 2: Using range() with two arguments")
for i in range(2, 6):  # Generates numbers from 2 to 5
    print(i)

# Example 3: Using range() with three arguments
print("\nExample 3: Using range() with three arguments")
for i in range(1, 10, 2):  # Generates numbers from 1 to 9 with a step of 2
    print(i)


# Example 4: Using range() to iterate over a list of numbers
print("\nExample 4: Using range() to iterate over a list of numbers")
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):  # Iterates over the indices of the list
    print(f"Index: {i}, Value: {numbers[i]}")

# Example 5: Using range() to create a countdown 
print("\nExample 5: Using range() to create a countdown")
for i in range(5, 0, -1):  # Generates numbers from 5 to 1 in reverse order
    print(i)


# Example 6: Using range() to create a list of even numbers
print("\nExample 6: Using range() to create a list of even numbers")
even_numbers = list(range(0, 21, 2))  # Generates even numbers from 0 to 20
print(even_numbers) 



# Example 7
list_f = [1, 2,3,4, 5, 6, 8,9 ]
for index in range(0, len(list_f)):
    print("Index: ", index)

    if index == 2:
        print("Elemento encontrado")


# using function enumerate() to iterate over a sequence and get both the index and the value of each item in the sequence.
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object. 

list_enumerate = ["apple", "banana", "cherry"]
for index, value in enumerate(list_enumerate):
    print(f"\nIndex = {index}, Value = {value}")
    
