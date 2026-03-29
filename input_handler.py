def get_choice():
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return choice
        print("Invalid choice. Please select a number from 1 to 5.")


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")
