# display.py

def show_menu():
    print("\n=== Simple Calculator ===")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (×)")
    print("4. Divide (÷)")
    print("5. Exit")

def show_result(num1, num2, operation, result):
    symbols = {'1': '+', '2': '-', '3': '×', '4': '÷'}
    print(f"{num1} {symbols.get(operation, '?')} {num2} = {result}")