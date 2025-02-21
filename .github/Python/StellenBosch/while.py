# Create variable to store the number increments entered by the user
total_sum = 0
# Create second variable to keep count of number of times user enters a number
entry_count = 0
# Ask the user to enter a number. with '-1' being acting as a kill switch/ end point
number = 0 
# Write a while loop and tell the program to run as long as the input is not (!=) -1
# Tell the program to save each interation while the condition is not met to the variable 'num1'
while number != -1:
    total_sum += number
# Tell the program to count each interation as the user is promted
    entry_count += 1
# When the while condition is not met, the program should keep running in iterations triggered by the condition not being met
    number = int(input("Please enter a number (enter -1 to exit) : "))
# If the number entered becomes '-1', the programe should check if the number of counts excluding '-1' are greater than 0.
# If the user has other entries either that '-1'. Let the user know the average of the value of entries
# To clean up this figure, insert the int() function to round the number
if number == -1:
    if entry_count > 0:
            print(f"The average value for the numbers you've entered is : {int(total_sum/entry_count)}")