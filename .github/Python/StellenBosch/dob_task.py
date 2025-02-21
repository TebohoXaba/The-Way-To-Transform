# Print the section heading 'Names: '
print("\nNames: \n")

# Open DOB.txt in read mode under the variable name 'source'
# This file will be openned in the directory, if it does not exist, program will fail
source = open('DOB.txt', 'r')
# Write a for loop statement where for every line in file/ variable 'source'
        # Use split() for split the lines to enable the separation of the names and dates...
        # ...and declare this modification to the variable 'Name'
        # To finish, print() Names. Use indexing inside the brackets of print() to select the...
        # ...first 2 positions in the lines of the text file which are name and surname
        # NB. create spaces between the words.
for line in source:
        Names = line.split()
        print(Names[0] + " " + Names[1])

# Close file not openned using the with/as method
source.close()

# Print the section heading 'Birth Dates: '
print("\nBirth Dates: \n")

# Open DOB.txt in read mode under the variable name 'source'
# This file will be openned in the directory, if it does not exist, program will fail
source = open('DOB.txt', 'r')
# Write a for loop statement where for every line in file/ variable 'source'
        # Use split() for split the lines to enable the separation of the names and dates...
        # ...and declare this modification to the variable 'DOB' (Date of Birth)
        # To finish, print() DOB. Use indexing inside the brackets of print() to select the...
        # ...last 3 positions in the lines of the text file which are the day, month, and year
        # NB. create spaces between the words.
for line in source:
        DOB = line.split()
        print(DOB[2] + " " + DOB[3] + " " + DOB[4])

# Close file not openned using the with/as method
source.close()