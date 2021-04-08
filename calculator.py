# calculator
user_operation = input("Choose: +, -, * or /: ")
user_number1 = float(input("Enter your first number: "))
user_number2 = float(input("Enter your second number: "))

addition = user_number1 + user_number2
subtraction = user_number1 - user_number2
multiplication = user_number1 * user_number2
division = user_number1 / user_number2

if user_operation == "+":
    print(addition)
elif user_operation == "-":
    print(subtraction)
elif user_operation == "*":
    print(multiplication)
elif user_operation == "/":
    print(division)
else:
    print(str(user_number1) + " " + str(user_operation) + " " + str(user_number2) + " = error")
