# Create an input variabe to capture the number of students registering for the exam venue
students = int(input("\nHow many students are registering: \n"))

# Open reg_form.txt in write mode under the variable name 'Register
# This file will either be overriden or a new one will be created...
# ...depending on whether it exists in the directory or not
# Write heading 'Register:' in your text file for readeability
# Close file where with/as method is not used for system efficiency
Register = open('./Task 11/reg_form.txt', 'w')
Register.write("Register: \n")
Register.close()

# Wtite a for loop statement where, for every student (recorded as i), in the number of students (recorded as students)
    # The loop must iterate to collect each students ID number through user prompt/input()
    # In every iteration, the value of i increases and represents the individual student...
    # ... i is used as a student identifier as well in the prompts
for i in range(students):
    i = i + 1
    student_number = input(f"\nPlease enter student {i}'s student number: \n")

    # Using the with/as method to open the reg_form.txt file, with the append argument as mode
        # Write each student number inputed by user through each iteration
        # Create dotted line for signatures from students who sign the register
    with open('./Task 11/reg_form.txt', 'a+') as f:
        f.write(student_number+": ................\n")

# Print a user message to confirm registration
print(f"\nCongratulations, you have successfully registered {students} students for the exam vanue!")