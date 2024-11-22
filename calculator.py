class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers.")
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers.")
        return a - b

    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers.")
        return a * b

    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers.")
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers.")
        return a ** b


if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Calculator!")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "6":
            print("Goodbye!")
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == "1":
                print("Result:", calc.add(a, b))
            elif choice == "2":
                print("Result:", calc.subtract(a, b))
            elif choice == "3":
                print("Result:", calc.multiply(a, b))
            elif choice == "4":
                print("Result:", calc.divide(a, b))
            elif choice == "5":
                print("Result:", calc.power(a, b))
            else:
                print("Invalid choice. Try again!")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except TypeError as te:
            print(f"Type error: {te}")
