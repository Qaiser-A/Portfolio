# Shopping cart program

# Create 2 empty lists

foods = []
prices = []

total = 0

# A while loop will allow the user to continue entering food to the cart until they quit

while True:
	food = input("Enter a food to buy (q to quit): ")
	# The .lower method will temporarily put the input as lowercase, so it will exit even when "Q" is entered
	if food.lower() == "q":
		break
	else:
		# The f string is used to insert a variable into a string, so in this case the food the price will be set for
		# Float is used to specify the type being used for the price when entered by the user
		# The .append method is used to add the foods and prices entered into the lists of the same names at the start of the program
		price = float(input(f"Enter a price for a {food}: £"))
		foods.append(food)
		prices.append(price)

print("---- Your Cart ----")

# Using a for loop to iterate over every food in the foods list and print them
for food in foods:
	print(food)

# Iterate and add up the prices for each food in the list
# To add up the total it's as it's quicker to use += and the same as than typing "total = total + price"
for price in prices:
	total += price

print(f"Your total is: £{total}")