# Methods
"""
These are immutable methods, meaning they do not change the original string but return a new string with the modifications applied.
"""

# .upper() - Converts all characters in a string to uppercase.

full_name = "Fernando Futila"
print(full_name.upper())  # Output: FERNANDO FUTILA

# .lower() - Converts all characters in a string to lowercase.
print(full_name.lower())  # Output: fernando futila



# Accessing individual characters in a string using indexing. Strings are zero-indexed, meaning the first character is at index 0.
first_char = full_name[0]
print(first_char)
