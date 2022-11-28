# importing Date and time
from datetime import datetime

#Getting the date and time and storing in a variable called "current"
current = datetime.now()

#Changing the format oh how date and time are displayed in D/M/Y and H:M:S and storing it in a variable called "format"
format = current.strftime('%d/%m/%y %H:%M:%S')


#Outputting the date and time in the format stated above
print('The date and time is ', format )
