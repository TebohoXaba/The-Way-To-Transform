# Ask user for their full name using input function with instruction in string
full_name = input("Please enter your full name : ")

# Create if statement to check the length of the input by the user to check if the input is empty
# if the input is empty, program should display error and prompt to user to enter full name
if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")
# Create 'else if' statement to check the length of the input by the user to check if the input is less than 4 charaters
# if the input is less than 4 charaters, program should display error and prompt to user to enter full name
elif len(full_name) < 4 :
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
# Create 'else if' statement to check the length of the input by the user to check if the input is more than 25 charaters
# if the input is more than 25 charaters, program should display error and prompt to user to ensure they have entered full name
elif len(full_name) >= 25 :
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
# if none of the above statements are satisfied. This means that else is activated as the end of the loop (exit)
# Insert else statement telling the program to thank the user for entering their full name
else :
    print("Thank you for entering your name.")