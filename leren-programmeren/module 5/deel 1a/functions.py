def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

result = 0
while True:
    choice = input("What would you like to do? A) Add numbers,\n B) Subtract numbers,\n C) Multiply numbers,\n D) Divide numbers,\n E) Increment,\n F) Decrement,\n G) Double,\n H) Halve,\n I) Nothing: ")
    if choice == "A":
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = addition(n1, n2)
    elif choice == "B":
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = subtraction(n1, n2)
    elif choice == "C":
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = multiplication(n1, n2)
    elif choice == "D":
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = division(n1, n2)
    elif choice == "E":
        n1 = float(input("Enter the number: "))
        result = addition(n1, 1)
    elif choice == "F":
        n1 = float(input("Enter the number: "))
        result = subtraction(n1, 1)
    elif choice == "G":
        n1 = float(input("Enter the number: "))
        result = multiplication(n1, 2)
    elif choice == "H":
        n1 = float(input("Enter the number: "))
        result = division(n1, 2)
    elif choice == "I":
        break
    else:
        print("Invalid input")
        continue

    print("Result:", result)

    next_operation = input("Would you like to do something with the result ({})?\n A) Add,\n B) Subtract,\n C) Multiply,\n D) Divide,\n E) Increment,\n F) Decrement,\n G) Double,\n H) Halve,\n I) Nothing: ".format(result))
    if next_operation == "I":
        break
    choice = next_operation