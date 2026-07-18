"""
Python is dynamically typed, meaning it identifies the text type by the presence of quotation marks. 
There are several ways to declare a text variable; the simplest is using double or single quotation marks.
It's also possible to use three quotation marks before and after the text to allow for line breaks. 
Another option is to use a backslash to break the text into two lines. It's recommended to use double quotation marks by default. 
Furthermore, we'll declare some text variables, such as full name, first name, and last name.

"""


# Declaration
full_name = "Fernando Futila"


full_name_with_triple = """Fernando 
Futila"""


full_name_with_backslash = "Fernando \
Futila"

name = "Fernando"
surname = "Futila"




"""
String formatting in Python. 
There are several ways to format variables within a string.
 The first way is to use a comma to concatenate the variable with the text. 
 This automatically adds a space between the text and the variable. 
 The second way is to use the plus sign (+) to concatenate the variable with the text, but without adding a space. 
 The third way is to use the plus sign (+) to concatenate multiple variables together. 
 We can add spaces manually using empty spaces or line breaks. We can also use both the comma and the plus sign to format strings. 
 Finally, we'll explore the difference between declaring a variable with quotation marks and with line breaks.


"""


# Formatting with 
print("Full name (1ª way):", full_name)
print("Full name (2ª way):" + full_name)
print("Full name (3ª way):" + "Fernando" + "Futila")
print("Full name (4ª way):" + "Fernando", "Futila")
print("Full name (5ª way):", full_name_with_triple)
print("Full name (6ª way):", full_name_with_backslash)

print("Full name (7ª way): %s" % full_name)
print("Full name (8ª way): %s %s" % (name, surname))

print(f"Full name (9ª way): {name} {surname}")

print("Full name (10ª way): {} {}".format(name, surname) )
