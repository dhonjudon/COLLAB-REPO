# main.py

from operations import add, subtract, multiply, divide
from display import show_menu, show_result
from input_handler import get_choice, get_numbers

def main():
    print("Welcome to Simple Calculator!")
    
    while True:
        show_menu()
        choice = get_choice()
        
        if choice == '5':
            print("Thank you for using the calculator! Goodbye 👋")
            break
        
        num1, num2 = get_numbers()
        
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        show_result(num1, num2, choice, result)
        
        # Ask to continue
        again = input("\nDo you want to do another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator! Goodbye 👋")
            break

if __name__ == "__main__":
    main()