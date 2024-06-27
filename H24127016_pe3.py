#coding : utf-8

print("WELCOME TO THE CALCULATOR!")

while True :

	num1 = float(input("\nEnter the first number : "))
	num2 = float(input("\nEnter the second number : "))

	operation = input("\nSelect an operation (+, -, *, /) : ")

	if operation == "+" :

		result = num1 + num2
		print(f"\nThe result of {num1} + {num2} is {result}")

	elif operation == '-' :
		result = num1 - num2
		print(f"\nThe result of {num1} - {num2} is {result}")

	elif operation == '*' :
		result = num1 * num2
		print(f"\nThe result of {num1} * {num2} is {result}")

	elif operation == '/' :
		if num2 == 0 :
			print("\nDivision by zero is not allowed. Please enter the numbers again.")
			continue

		result = num1 / num2
		print(f"\nThe result of {num1} / {num2} is {result}")

	else :
		print("\nInvalid operation. Please select a valid operation.")
		continue

	another_calculation = input("\nDo you want to perform another calculation? (yes/no): ")

	if another_calculation == 'yes' :
		continue
	else :
		print("\nGoodbye!")
		break