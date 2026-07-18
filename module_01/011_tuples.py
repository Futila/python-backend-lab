# Tuple - Immutable ordered collection of elements.

# 1. Creating a tuple

my_tuple = (1, 2, 3, 4, 5)

print("My tuple: ", my_tuple)

# 2. Accessing elements in a tuple
print("First element of my tuple is:", my_tuple[0])
print("Last element of my tuple is:", my_tuple[-1])



# Method count() - Returns the number of occurrences of a specified element in the tuple.
count_of_2_in_tuple = my_tuple.count(2)
print("Count of 2 in my tuple is: ", count_of_2_in_tuple)