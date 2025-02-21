# Ask for user input between 1 and 10
# Convert string to integer for easier processing later
user_input = input("Please enter a number between 1 and 10: ")
user_number = int(user_input)

# Wriet if statement where if user number is greater than 0
# Program saves the symbol '*' under variable star
if user_number > 0: 
    star = "*"
    # Write a for loop where for every i (variable) in the range() of the index (being between 0 and the user_number/input)
    # Program should add a star, for every iteration of this index being read, the program should add one more star
    for i in range(0 ,user_number):
        print(star)
        # Logic Error: My chosen Logic error is simple, instead of adding the string "*" to my for loop
        # i referenced (added) the variablle 'star' again
        star = star + star 

# Wriet if statement where if user number is greater than 0
# Program saves the 10 '*' symbols under variable star
if user_number > 0:    
    stars = "***********"
    # Write a for loop where for every i (variable) in the range() of the index (being between 0 and the user_number/input)
    # Program should subtract a star represented by user_number -1 in brackets, for every iteration of this index being read;
    # The program should subtract one more star at every print()
    for i in range(0 ,user_number):

        index = (user_number-1) -i
        print(stars[0:index])