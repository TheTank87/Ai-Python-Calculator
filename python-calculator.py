import math
import random


# --- PART 1: MINESWEEPER MODULE ---
class Minesweeper:
    def __init__(self, size=8, mines=10):
        self.size = size
        self.num_mines = mines
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.visible_board = [["-" for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.game_over = False
        self.revealed_count = 0

    def place_mines(self):
        while len(self.mines) < self.num_mines:
            r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))
                self.board[r][c] = "*"

    def calculate_neighbors(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == "*":
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size:
                            if self.board[nr][nc] == "*":
                                count += 1
                self.board[r][c] = count

    def reveal(self, r, c):
        if (
            not (0 <= r < self.size and 0 <= c < self.size)
            or self.visible_board[r][c] != "-"
        ):
            return
        if self.board[r][c] == "*":
            self.game_over = True
            return
        self.visible_board[r][c] = str(self.board[r][c])
        self.revealed_count += 1
        if self.board[r][c] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    self.reveal(r + dr, c + dc)

    def print_board(self):
        print("\n   " + " ".join(str(i) for i in range(self.size)))
        print("  " + "---" * self.size)
        for i, row in enumerate(self.visible_board):
            print(f"{i} | {' '.join(row)}")

    def play(self):
        self.place_mines()
        self.calculate_neighbors()
        print("\n--- MINESWEEPER MODE ---")
        while not self.game_over:
            self.print_board()
            try:
                move = (
                    input("\nEnter Row and Column (e.g., '2 3') or 'back': ")
                    .strip()
                    .lower()
                )
                if move == "back":
                    break
                r, c = map(int, move.split())
                self.reveal(r, c)
                if self.revealed_count == (self.size**2 - self.num_mines):
                    self.print_board()
                    print("\nWINNER! You cleared the board!")
                    break
            except:
                print("Invalid move. Use 'Row Column' format.")
        if self.game_over:
            print("\nBOOM! Game Over.")


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
    print("Type 'minesweeper' for Game.")
    print("Type 'credits' to go see contributions.")
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


def show_credit():
    """Shows who made this program"""
    print("█████████████████████████████████████████")
    print("█─▄▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█▄─▄█─▄─▄─█─▄▄▄▄█")
    print("█─███▀██─▄─▄██─▄█▀██─██─██─████─███▄▄▄▄─█")
    print("▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀")
    print(" ")
    print(" ")
    print(" ")
    print("Made by TheTank87")
    print(
        "Website: https://tdf-the-diat-formation.fandom.com/wiki/T.D.F._The_Diat_Formation_Wiki"
    )


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
    elif choice == "minesweeper":
        game = Minesweeper()
        game.play()
    elif choice == "credits":
        show_credit()
    elif choice == "off":
        print("Powering off...")
        break  # Initiates a break to exit the program [3]
    else:
        print("Unknown Command.")
