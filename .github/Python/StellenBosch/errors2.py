# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Syntax error: Missing quotation marks for indicate Lion is a String
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# Run Time Error: Included "f" for (format.) before by string to allow it to cast variables inside string
# and used {} brackets to reference my variables
# Logic error: the variables animal_type and number_of_teeth were swapped out

print(full_spec) # Syntax Error: Missiing brackets for print function

