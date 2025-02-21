# Print heading for alternate charaters section
print("Alternate Character:\n")
# Save a sentence under the variable 'original_string
# Create a variable for storing every alternate charater for my for loops
original_string = "This is my alternate string for this compulsory task!"
alternate_char = ""
# Write a for loop statement to read the original_string
# with an if statement with the condition to check the original_string
# Where for every even concatenation of number (index), ...
# ...The variale storage 'alternate_char' stores those characters as upper case
# And (else statement) where this condition (if statement) is not satisfied, ... 
# ...The variale storage 'alternate_char' stores those characters as lower case
for i in range(len(original_string)):
    if i % 2 == 0:
        alternate_char += original_string[i].upper()
    else:
        alternate_char += original_string[i].lower()
# Finally, print the updated stored characteres and create a line spacing
print(alternate_char, "\n")
# Print heading for alternate word section
print("Alternate Word:\n")
# Create a variable where the original_string is manipulated by splitting the words, ...
# ...Where they can be used or further manipulated later
# Then create a storage variable where each alternate word in the for loop will be stored
original_words = original_string.split()
alternate_word = ""
# Write a for loop statement to read the original_words variable
# With an if statement with the condition to check the original_words
# Where for every second instance where i is equal to an even placement/ index
# ...The variale storage 'alternate_word' stores those words in lower case
# And (else statement) where this condition (if statement) is not satisfied, ... 
#  ...The variale storage 'alternate_word' stores those words in the list as upper case
for i in range(len(original_words)):
    if i % 2 == 1:
        alternate_word += original_words[i].lower() + " "
    else:
        alternate_word += original_words[i].upper() + " "
# Finally print the updated alternate_word where every odd (first) word is upper case
print(alternate_word)