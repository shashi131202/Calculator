# Calculator CLI App

# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

# Main Program
while True:
    print("\n--- Calculator Menu ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Exiting... Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select from 1-5.")
