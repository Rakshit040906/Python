# Basic Calculator Program

def run_calculator():
    print("Simple Calculator")
    
    # Get numbers from user
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    
    # Display available operations
    print("Select operation:")
    print(" +  for addition")
    print(" -  for subtraction")
    print(" *  for multiplication")
    print(" /  for division")
    
    operator = input("Enter operator (+, -, *, /): ")

    # Perform the chosen operation
    if operator == '+':
        result = first + second
    elif operator == '-':
        result = first - second
    elif operator == '*':
        result = first * second
    elif operator == '/':
        if second != 0:
            result = first / second
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid operator selected.")
        return

    # Display the result
    print(f"Result: {first} {operator} {second} = {result}")

# Start the calculator
run_calculator()




