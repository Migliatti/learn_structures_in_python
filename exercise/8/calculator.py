# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

#     Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
#     Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.
import os

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print("Calculator Menu")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Choose an operation (1-4): "))

    if choice in [1, 2, 3, 4]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == 1:
                print(f"Result: {sum(num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"Result: {divide(num1, num2)}")
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input. Please enter numeric values.")
            calculator()
        except ZeroDivisionError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error: Division by zero is not allowed.")
            calculator()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please select a valid operation.")
        calculator()

calculator()