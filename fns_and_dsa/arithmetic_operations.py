# Define the perform_operation function
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"  # Handle division by zero
        return num1 / num2
    else:
        return "Invalid operation"  # Handle invalid operations