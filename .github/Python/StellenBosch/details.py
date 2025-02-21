"""
# user must enter their name
# user must enter their age
# convert age of user to int()
# user must enter their House Number
# convert House Number of user to int()
# user must enter their street name
# program print() to display users details
"""

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
house_number = int(input("Please enter your house number: "))
street_name = input("Please enter your street name : ")
print(f"This is {name}. He is {age} and lives at house number {house_number} on {street_name}")