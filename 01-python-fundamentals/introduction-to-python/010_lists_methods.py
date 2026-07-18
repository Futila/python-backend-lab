# Lists Methods - Common operations that can be performed on lists.

# 1. append() - Adds an element to the end of the list.
my_list = [1, 2, 5, 5, "Futila", 6,7, 3]
my_list.append(6)

print(" My list after append: ", my_list)


# 2. index() - Returns the index of the first occurrence of an element in the list.
index = my_list.index(7)
print("Index of 7 in my_list:", index)


# 3. insert() - inserts an element at a specified index in the list.
my_list.insert(2, 99)
print("My list after insert: ", my_list)


# 4. pop() - Removes and returns the element at the specified index. If no index is specified, removes and returns the last element.
popped_element = my_list.pop(3)
print("My list after pop: ", my_list)
print("Popped element: ", popped_element)

# 5. remove() - Removes the first occurrence of an element from the list.
my_list.remove(5)
print("My list after remove: ", my_list)

# 6. sort() - Sorts the elements of the list in ascending order.
my_list.sort()
print("My list after sort: ", my_list)