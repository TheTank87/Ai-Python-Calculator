def ask_to_continue():
    """Asks the user if they wantto perform another calculation."""
    # input() reads the response as a string [4, 5]
    # .lower() ensures 'YES' or 'Yes' are treated the same as 'yes' [6, 7]
    choice = input("Do you want to start another calculation? (yes/no): ").lower()

    # Returns True if the user wants to continue, otherwise False [8, 9]
    return choice == "yes"


# A while True loop creates an infinite loop until a break is triggered [10, 11]
while True:
    # 1. Obtain input from the user
    num1 = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # 2. Use conditional logic (if-elif-else) to select the operation [12-14]
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Error! Division by zero is not allowed."[15, 16]
    else:
        result = "Invalid operation selected."

    # 3. Display the result
    print(f"Result: {result}")

    # 4. Call the function to see if the user wants to restart [17, 18]
    if not ask_to_continue():
        print("Exiting DIAT calculator! System shutting down...")
        break  # Exits the while loop [19, 20]
