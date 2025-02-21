'''Write code to output the star pattern shown below, using an if-else
statement in combination with a single for loop (it’s really easy with two
but using only one takes a little more thought!):
*
**
***
****
*****
****
***
**
*
'''

# Print out the first section of my task where i demonstrate the use of 2 separate blocks of code
print("Using two if statements and two for loops: ")
# Assign the variable name given_name to 5
given_number = 5
# Write an if statement where if given_number is greater than 0 (contains data) = statement runs
if given_number > 0:
        # Declare the variable star to save the symbol *
        star = "*"
        # Write a for loop, where the variable "i" in range between 1st and 6th position are within scope
        # Write print() function where teh variable star is printed out in increments of 1 star at every iteration
        for i in range(0 ,5):
                print(star)
                star = star +"*"
# Wrte if statement where if given_numebr is greater than 0 (statement runs)
if given_number > 0:
            # Declare the variable for storing 5 stars and write for loop, where:
            # i in range from first place till 5th place, excluding 5th place is looked at
            stars = "*****"
            for i in range(0 ,4):
                # Create an index alteration for every iteration in the loop, where 4 minus the current value of i
                # Go on to print the stars from 5 decreasing till it gets to 1 star
                index = 4-i
                print(stars[0:index]) 
# Write print() function to indicate new section where one of each statement and/or loop will begin
print("")
# Print the second section where method 2 is writen
print("Using one if statement and one for loop: ")
# Declare variable for 5 as given number
given_number = 5
# Write if statement, where if given_number is > 0 = run
if given_number > 0:
    # The for loop runs between a range of 1 to 9 for context, where the 2 is multiplied by 5 (given number) minus 1 (iterations)  (2 * 5 - 1)
    for i in range(1, 2 * given_number):
        # Write if statement for if number of iterations is less than or equal to 5 (given number) 
        # Write print() function to tell python to print a star, and add one more star at every iteration stored in i variable
        if i <= given_number:
            # Increasing stars for the first half
            print("*" * i)
        # Write else statement to tell the program to start printing the stars in reverse
        else:
            # Decreasing stars for the second half
            print("*" * (2 * given_number - i))
# Print a line space to show end of code before remarks
print("")
# Thanks for the challeng!
print("Thanks for the challeng!")
#End python code
print("")
print("The End")
print("")