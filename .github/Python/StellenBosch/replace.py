# Declare the variable single_string for the single string word "The!quick!brown!fox!jumps!over!the!lazy!dog"
single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog" 
# Then slice the word using the replace() function by replacing the symbol "!" with an emply space
single_string = single_string.replace("!", " ")
# Print the new sentance. start by referencing which variable is being printed, use format.() to let the programe know which format to return
print("single_string.replace(""!"", " "): {}".format(single_string))

# Turn string unto upper case letters only, i can use .upper() function declared to the variable single_string
single_string = single_string.upper()
# Print using the .upper() format by referencing the single_string.upper() string method variable
print(f"single_string.upper() : {single_string}")

# Print the sentence in reverse through reverse indexing, -1 tells the program to start at the end point of the sentence. 
# By not referencing after the fits collon, i tell the program to find and end at the first letter of the sentence. The second -1 is to tell the program to record every position till its end point.
print(single_string[-1: :-1])