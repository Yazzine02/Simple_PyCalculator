def calculator():
	print("Welcome to your friendly neighborhood calculator")
	while True:
		print("Please enter the appropriate number according to your needs")
		print("1. Addition")
		print("2. Substraction")
		print("3. Multiplication")
		print("4. Division")
		print("0. Exit")
		option = int(input("Enter your option: "))
		if option == 0:
			print("Exiting the program. Goodbye!")
			break	
		get_user_option_input(option)
		continue_calculator = input("Do you want to continue? (y/n): ")
		while continue_calculator.lower() != 'y' and continue_calculator.lower() != 'n':
		#Use AND not OR logic because it can be equal to "y" and still different to "n" => infinite loop
			continue_calculator  = input("Please select either y or n:")
		if continue_calculator.lower() == 'n':
            		break
	
def get_user_option_input(option):
	try:
            if option not in range(1, 5):
            	print("Invalid option. Please enter a number between 1 and 4.")
            	return
	except ValueError:
	    print("Invalid input. Please enter a number.")
	    return
        
	match option:
		case 1:
			print("You selected addition")
		case 2:
			print("You selected substraction")
		case 3:
			print("You selected multiplication")
		case 4:
			print("You selected division")
	result = get_result(option)
	print("Result: ", result)
			
def get_result(option):
	while True:
		try:
			firstNumber = float(input("Enter first number: "))
			secondNumber = float(input("Enter second number: "))
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue
		match option:
			case 1:
				return firstNumber + secondNumber
			case 2:
				return firstNumber - secondNumber
			case 3:
				return firstNumber * secondNumber
			case 4:
				if secondNumber == 0:
					print("Please enter a non 0 value for the second number")
					continue
				return firstNumber / secondNumber

calculator()
