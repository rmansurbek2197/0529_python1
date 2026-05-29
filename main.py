class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"Added {num1} and {num2}. Result: {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"Subtracted {num2} from {num1}. Result: {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"Multiplied {num1} and {num2}. Result: {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2
        self.history.append(f"Divided {num1} by {num2}. Result: {result}")
        return result

def main():
    calculator = Calculator()
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. History")
        print("6. Exit")
        choice = input("Choose an operation: ")
        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {calculator.add(num1, num2)}")
        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {calculator.subtract(num1, num2)}")
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {calculator.multiply(num1, num2)}")
        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            try:
                print(f"Result: {calculator.divide(num1, num2)}")
            except ZeroDivisionError as e:
                print(e)
        elif choice == "5":
            for history in calculator.history:
                print(history)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()