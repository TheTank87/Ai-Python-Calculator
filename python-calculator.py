def welcome_page():
    """Introduces the program and handles the start/off selection."""
    print("------------------------------------")
    print("Welcome to the Potato Calculator!")
    print("Type 'start' to begin or 'off' to exit.")
    print("------------------------------------")

    # input() reads the user's choice as a string
    choice = input("Your selection: ").lower()
    return choice


def run_calculator():
    """Main calculator logic from the previous program."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Enter an operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                # Division by zero handled in previous conversation
                result = num1 / num2 if num2 != 0 else "Error! Division by zero."
            else:
                result = "Invalid operation."

            print(f"Result: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")

        # Ask if they want another calculation before going back to the welcome page
        again = input("Do you want to start another calculation? (yes/no): ").lower()
        if again != "yes":
            break


# The program starts here
while True:
    user_choice = welcome_page()

    if user_choice == "start":
        run_calculator()
    elif user_choice == "off":
        print("Powering off...")
        break  # Initiates a break to exit the program
    else:
        print("Invalid selection. Please type 'start' or 'off'.")
