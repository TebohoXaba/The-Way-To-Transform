# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax Error: Missiing brackets for print function
print("\n") # Syntax Error: Missiing brackets for print function

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax error: I removed the uneccessary words "years old" 
# because the programe cant convert string with words, and removed the uneccessary = sign as well 

# Variables declaring the user's age, casting the str to an int, and printing the result
age = int(age_Str) 
print("I'm" + " "+ str(age) + " " + "years old.") 
# Run Time error: age is an integer and can not be used in the same instance as strings.
# Cast str() to int. Added empty strings for spacing as well

# Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now # Run Time error: years_from_now should be converted into number

print("The total number of years: " + str(total_years))  # Syntax Error: Missiing brackets for print function
# Additional runtime error for not converting "total_years" to string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6
# Syntx Error: Missing variable name where variable was "total" instead of "total_years"
# Logic error: missing 6 months added
print("In 3 years and 6 months, I'll be" + " " + str(total_months) + " " + "months old") # Syntax Error: Missiing brackets for print function
# Run time error: missing str() function to convert total_months to string

#HINT, 330 months is the correct answer

