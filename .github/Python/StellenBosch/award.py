# ask participant for triathon minutes
# instantly cnvert their inputs to integers using int() or float using float() for easier calculations later
# save participant responses in variables named after each triathon activity/ sport
swimming = int(input(("How many minutes did you swim for : ")))
cycling = int(input("How many minutes did you cycle for : "))
running = int(input("How long did you run for : "))
# calculate the total time using the '+' operator
# save this new number (total time) in a variable to use later
total_time = swimming + cycling + running
# print sttatement "Total time taken for the triathon: {} minutes" and insert the variable storing the 'toatl time'
print(f"Total time taken for the triathon: {total_time} minutes")
'''
create if statement for the award for finishing the triathon within the recommended time of 0 to 100 minutes
create an elif (else if) statement to print out a performance result for participants that finished within 5 minutes above the recommended time
create a second elif statement for partcipants ho finish the triathion later than 105 minutes
create a thrid elif statements for anyone who ultimately does not finish the race with the maximum time of 110 minutes
create an else statement for error handling purposes that prints out a try again string for participants that could not satisfy any of the if or elif statements
'''
if total_time <= 100 :
    print("Award: Provincial colours")
elif total_time > 100 :
    print("Award: Provincial half colours")
elif total_time > 105 :
    print("Award: Provincial scroll")
elif total_time > 110 :
    print("No Award")
else:
    print("System error. Please try again")