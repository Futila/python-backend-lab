# More methods


# .count() - Counts the number of occurrences of a substring in the string.
sentence = "The quick brown fox jumps over the lazy dog. The dog barked."
count_e = sentence.count("e")
print("Count (e):", count_e)



# .find() - Returns the index of the first occurrence of a substring in the string. Returns -1 if the substring is not found.
index_over = sentence.find("over")
print("Index of over: ", index_over)


# .encode() - Encodes the string into bytes using the specified encoding. The default encoding is UTF-8.
encoded_sentence = sentence.encode("utf-8")
print("Encoded sentence:", encoded_sentence)


# .decode() - Decodes bytes back into a string using the specified encoding. The default encoding is UTF-8.
decoded_sentence = encoded_sentence.decode("utf-8")
print("Decoded sentence:", decoded_sentence)



# .replace() - Replaces occurrences of a substring with another substring in the string.
new_sentence = sentence.replace("fox", "fax")
print("New sentence:", new_sentence)

# we can use multiple replace() methods to replace multiple substrings in a string.
new_sentence_multiple = sentence.replace("fox", "fax").replace("dog", "cat")
print("New sentence with multiple replacements:", new_sentence_multiple)


# .join() - Joins a list of strings into a single string, with a specified separator.
words = ["The", "quick", "brown", "fox"]
joined_sentence = " ".join(words)
print("Joined sentence:", joined_sentence) 



# .slipt() - Splits the string into a list of substrings based on a specified separator. The default separator is whitespace.
full_name = "Fernando Futila"
slplitted_name = full_name.split()
print("Splitted name:", slplitted_name)



# .strip() - Removes leading and trailing whitespace from the string.
name_with_spaces = "   Fernando Futila   "
stripped_name = name_with_spaces.strip()
print("Stripped name:", stripped_name) 



# .rstrip() - Removes trailing whitespace from the string.
name_with_trailing_spaces = "Fernando Futila   "
rstrip_name = name_with_trailing_spaces.rstrip()
print("Right stripped name:", rstrip_name)




# .startswith() - Returns True if the string starts with the specified substring, otherwise returns False.
starts_with_Fe = full_name.startswith("Fe")
print("Starts with 'Fe':", starts_with_Fe)



# comparator in - Returns True if the specified substring is found in the string, otherwise returns False.
contains_Futila = "Mendes" in full_name
print("Contains 'Futila':", contains_Futila)


# comparator not in - Returns True if the specified substring is not found in the string, otherwise returns False.
not_contains_Mendes = "Mendes" not in full_name
print("Does not contain 'Mendes':", not_contains_Mendes)