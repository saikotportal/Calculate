from calculator import Calculator


MENU = """
╔══════════════════════════════╗
║     PYTHON CALCULATOR CLI    ║
╠══════════════════════════════╣
║  1. Add          (+)         ║
║  2. Subtract     (-)         ║
║  3. Multiply     (×)         ║
║  4. Divide       (÷)         ║
║  5. Power        (^)         ║
║  6. Modulo       (%)         ║
║  7. View History             ║
║  8. Clear History            ║
║  0. Exit                     ║
╚══════════════════════════════╝
"""

OPERATIONS = {
    "1": ("add", "+"),
    "2": ("subtract", "-"),
    "3": ("multiply", "×"),
    "4": ("divide", "÷"),
    "5": ("power", "^"),
    "6": ("modulo", "%"),
}


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Please enter a valid number.")


def run():
    calc = Calculator()
    print("\nWelcome to the Python Calculator!")

    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("\nGoodbye! 👋\n")
            break

        elif choice in OPERATIONS:
            op_name, symbol = OPERATIONS[choice]
            print(f"\n  Operation: {symbol}")
            a = get_number("  Enter first number : ")
            b = get_number("  Enter second number: ")

            try:
                method = getattr(calc, op_name)
                result = method(a, b)
                print(f"\n  ✔  Result: {a} {symbol} {b} = {result}\n")
            except ZeroDivisionError as e:
                print(f"\n  ✘  Error: {e}\n")

        elif choice == "7":
            history = calc.get_history()
            if not history:
                print("\n  No history yet.\n")
            else:
                print("\n  --- Calculation History ---")
                for i, entry in enumerate(history, 1):
                    print(f"  {i}. {entry}")
                print()

        elif choice == "8":
            calc.clear_history()
            print("\n  ✔  History cleared.\n")

        else:
            print("\n  ⚠  Invalid choice. Please try again.\n")


if __name__ == "__main__":
    run()
