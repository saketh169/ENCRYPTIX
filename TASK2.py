# SIMPLE CALCULATOR

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    
choice = input ("ENTER YOUR CHOICE (1/2/3/4):")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print("RESULT OF CALCULATION ")
if choice == '1':
            print(f"{n1} + {n2} = {add(n1, n2)}")

elif choice == '2':
            print(f"{n1} - {n2} = {subtract(n1, n2)}")

elif choice == '3':
            print(f"{n1} * {n2} = {multiply(n1, n2)}")

elif choice == '4':
            print(f"{n1} / {n2} = {divide(n1, n2)}")
else:
        print("Invalid choice")

