import math


# Define custom functions for csc, sec, and cot since they are 1/trig_func
def csc(x):
    return 1 / math.sin(x)


def sec(x):
    return 1 / math.cos(x)


def cot(x):
    return 1 / math.tan(x)


def welcome_page():
    """Introduces the program and handles the start/off/help selection."""
    print("\n====================================")
    print("   SCIENTIFIC PYTHON CALCULATOR by:TheTank87")
    print(" ")
    print("██╗░░██╗░█████╗░░█████╗░██╗░░██╗░█████╗░████████╗██╗███╗░░░███╗███████╗")
    print("██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗╚══██╔══╝██║████╗░████║██╔════╝")
    print("███████║███████║██║░░╚═╝█████═╝░███████║░░░██║░░░██║██╔████╔██║█████╗░░")
    print("██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══██║░░░██║░░░██║██║╚██╔╝██║██╔══╝░░")
    print("██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║░░██║░░░██║░░░██║██║░╚═╝░██║███████╗")
    print("╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
    print(" ")
    print("====================================")
    print("Type 'start' to begin.")
    print("Type 'help' to see available functions.")
    print("Type 'off' to exit.")
    print("------------------------------------")
    return input("Selection: ").lower().strip()


def show_help():
    """Lists all available functions for the user."""
    print("\n--- Available Functions & Constants ---")
    print("Basic: +, -, *, /, ^ (exponent), ( )")
    print("Trig: sin, cos, tan, csc, sec, cot")
    print("Inverse Trig: asin, acos, atan")
    print("Logarithms: log (natural log), log10")
    print("Constants: pi, e")
    print("Example expression: (sin(pi/2) + log(10)) ^ 2")
    input("\nPress Enter to return to menu...")


def run_calculator():
    """Main expression evaluator logic."""
    print("\n--- Expression Mode ---")
    print("Enter your full math expression (or 'back' for menu):")

    # Environment for eval() to recognize trig/math functions safely
    safe_dict = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "csc": csc,
        "sec": sec,
        "cot": cot,
        "log": math.log,
        "log10": math.log10,
        "pi": math.pi,
        "e": math.e,
        "sqrt": math.sqrt,
    }

    while True:
        expr = input("> ").lower().strip()

        if expr == "back":
            break

        # Replace user '^' with Python's '**' operator [5, 6]
        expr = expr.replace("^", "**")

        try:
            # Evaluate the string as a mathematical expression [7, 8]
            result = eval(expr, {"__builtins__": None}, safe_dict)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")[3, 9]
        except Exception as e:
            print(f"Error: Invalid expression. Check your syntax. ({e})")[10, 11]


# Main program loop
while True:
    choice = welcome_page()

    if choice == "start":
        run_calculator()
    elif choice == "help":
        show_help()
    elif choice == "off":
        print("Powering off...")
        break  # Initiates a break to exit the program [3]
    else:
        print("Invalid selection. Please type 'start', 'help', or 'off'.")
