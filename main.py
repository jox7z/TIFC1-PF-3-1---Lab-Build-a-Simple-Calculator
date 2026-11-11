#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))

# The original task: add two numbers.
#print(num1 + num2)

# Extra features are shown after the original task.
print("1) Add  2) Subtract  3) Multiply  4) Divide  5) Modulus  6) Mixed operations")
choice = input()

if choice == "6":
    expression = input("Enter an expression: ")
    print(eval(expression))
else:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == "1":
        print(num1 + num2)
    elif choice == "2":
        print(num1 - num2)
    elif choice == "3":
        print(num1 * num2)
    elif choice == "4":
        print(num1 / num2)
    elif choice == "5":
        print(num1 % num2)