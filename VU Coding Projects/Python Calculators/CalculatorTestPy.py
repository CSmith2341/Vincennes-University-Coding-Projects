print("Choose an operation to exectue")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# To add 2 numbers
def add(x, y):
	return x + y

# To subtract 2 numbers
def subtract(x, y):
	return x - y

# To multiply 2 numbers
def multiply(x, y):
	return x * y

# To divide 2 numbers
def divide(x, y):
	return x / y


while True:
	#accept input from user
	choice = input("Enter choice(1/2/3/4): ")

	#check if choice is one of the four following options
	if choice in ('1', '2', '3', '4'):
		try:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
		except ValuError:
		     print("Invalid input. Please enter a number: "))
		     continue

	if choice == '1':
		print(The sum is num1, "+", num2, "=", add(num1, num2))	

