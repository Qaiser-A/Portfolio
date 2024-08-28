# Bank program

# Creating functions to show the balance, make a deposit and withdraw

def show_balance(balance):
	print("**************")
	print(f"Your balance is £{balance:.2f}") # The .2f will display the balance to 2 decimal places
	print("**************")

def deposit():
	amount = float(input("How much would you like to deposit? "))

	# Check to ensure the amount entered to deposit is more than 0
	if amount < 0:
		print("That's not a valid amount. You have to deposit more than £0")
		return 0 # We return 0 here to avoid any errors ocurring in the console
	else:
		return amount

def withdraw(balance):
	amount = float(input("How much would you like to withdraw? "))

	if amount > balance:
		print("Insufficient funds")
		return 0
	elif amount < 0:
		print("Amount must be more than 0")
		return 0
	else:
		return amount

def main():
	balance = 0 # Balance has to be parsed in the functions which use this local variable, show_balance and withdraw
	is_running = True # This will remain True as long as the program is running

	while is_running:
		print("**************") # This is just text decoration to make it look nicer when running  
		print("Welcome to Mystery Bank")
		print("**************")
		print("1. Show Balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Exit")

		# Stroing the user's input into the variable called "choice"
		choice = input("Enter your choice (1-4): ")

		# If the user entered 1 in the form of a string as per the input, then call the show balance method
		if choice == "1":
			show_balance(balance)
		elif choice == "2":
			balance += deposit() # Change the balance to reflect any deposits made
		elif choice == "3":
			balance -= withdraw(balance) # Change the balance to reflect any withdrawals made
		elif choice == "4":
			is_running = False
		else:
			print("That is not a valid choice") # If the user enters an invalid input then use the else statement to handle it

	print("Thank you for using our services") # When the program stops running, print this line

# This is good practice for importing the function or running standalone
if __name__ == '__main__':
	main() # Calls the main function above