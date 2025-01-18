def calculator():
    """
    A simple calculator program that performs basic arithmetic operations: addition, subtraction,
    multiplication, and division. It prompts the user to input two numbers and choose an operation,
    then displays the calculated result.
    """

    def get_number(prompt):
        """Prompt the user to input a number and handle invalid input."""
        while True:
            try:
                return float(input(prompt))  # Convert input to float for numerical operations
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operation():
        """Prompt the user to select a valid operation."""
        operations = {"1": "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Division"}
        print("\nSelect an operation:")
        for key, value in operations.items():
            print(f"{key}. {value}")

        while True:
            choice = input("Enter your choice (1/2/3/4): ")
            if choice in operations:
                return choice
            else:
                print("Invalid choice. Please select a valid operation.")

    print("Welcome to the Simple Calculator!")

    # Input numbers
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # Choose operation
    operation = get_operation()

    # Perform calculation based on selected operation
    if operation == "1":  # Addition
        result = num1 + num2
        operation_name = "Addition"
    elif operation == "2":  # Subtraction
        result = num1 - num2
        operation_name = "Subtraction"
    elif operation == "3":  # Multiplication
        result = num1 * num2
        operation_name = "Multiplication"
    elif operation == "4":  # Division
        if num2 != 0:
            result = num1 / num2
            operation_name = "Division"
        else:
            print("Error: Division by zero is not allowed.")
            return

    # Display result
    print(f"\n{operation_name} Result: {num1} and {num2} = {result}")

if __name__ == "__main__":
    calculator()
