# Conditionals and coverting data types

#Taking user input as a string as it cannot be taken as an int
age = input(str('What is your age? '))

#Converting the above data type (string) into integer for the conditions to run using the same data type
age = int(age)

#If, else if(elif) and else being used to determine age and print the following messages to the console
if age < 26:
    print('You are younger than 26')
elif age > 24:
    print ('You are older than 24')
else:
    print('You clearly have a different age')
