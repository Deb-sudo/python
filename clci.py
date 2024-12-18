# A simple calculator program in Python

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        # Take input from the user
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"The result is: {num1 + num2}")
            elif choice == 2:
                print(f"The result is: {num1 - num2}")
            elif choice == 3:
                print(f"The result is: {num1 * num2}")
            elif choice == 4:
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Error! Division by zero.")
        else:
            print("Invalid input")
    except ValueError:
        print("Please enter valid numbers.")

# Call the calculator function
if __name__ == "__main__":
    calculator()
