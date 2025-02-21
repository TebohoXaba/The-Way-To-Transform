# ask the user to type any sentence in the text bar and save the response to the variable str_manip
str_manip = input("Please Type a sentance here : ")
# display the length of the string entered by the user
print(len(f"{str_manip}"))
# determine and display the last lettter from the sentence entered by the user
# replace that letter with "@" for each of its occurences
# save this command to the variable str_manip
# print the updated variable 'str_manip'
str_manip = str_manip.replace(str_manip[-1: ], "@")
print(str_manip)
# print the last 3 words of the entry in reverse
print(str_manip[-1:-4:-1])
# print the first 3 letter of the sentence and the last 2 as one word
print(str_manip[0:3]+str_manip[-1:-3:-1])