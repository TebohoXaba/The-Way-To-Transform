# ask user to enter 3 different whole numbers, separating the promts feels more natural
# cobert all inputs into intergers using int()
numbers = [int(input("Please enter a number : ")), int(input("Please enter a second whole number : ")), int(input("Please enter a third whole number : "))]
# program should display the sum of the numbers entered into the list by user
print(f"{sum(numbers)}")
# program should display the value of the first number in the list subtracted by the second number in the list
print(f"{numbers[0] - (numbers[1])}")
# program should display the value of the third number in the list multiplied by the first number in the list
print(f"{numbers[2] * numbers[0]}")
# program should display the value of the sum of the list divided by the third number in the list
print(f"{sum(numbers) / numbers[2]}")