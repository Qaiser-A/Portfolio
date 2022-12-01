# Arrays and appending them

# Making an array and storing it in teams
# Can also use other data tpes in arrays
teams = ['England','Brazil','Argentina','Portugal','Spain','Italy']

print('Original list')
# A for loop being used to iterate and print every element in the array
for i in teams:
    print( i)

# Adds an element to the end of the array referencing the array itself
teams.append('Netherlands')

# \n is used to insert new lines
print('\n\nAmended list\n')

# Printing the updated array using a for loop again
for i in teams:
    print(i)
