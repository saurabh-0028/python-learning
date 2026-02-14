# Simple Calculator Project
# Author: Mr. Selfish 😎

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting Calculator. Bye 👋")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", sub(a, b))
    elif choice == "3":
        print("Result:", mul(a, b))
    elif choice == "4":
        print("Result:", div(a, b))
    else:
        print("Invalid choice")
