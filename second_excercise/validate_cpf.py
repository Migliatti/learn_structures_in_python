# Carlos works in a court and needs to validate if the CPF entered by the client is in the correct format before proceeding with the service. The CPF must contain exactly 11 numeric digits. If the entry contains letters or any other character that is not a number, the program must display an error message.

# Create a program that asks the user for a CPF number and verifies if it has 11 digits and contains only numbers.

def validate_cpf(cpf):
    print(cpf)

try:
    cpf = input("Enter the CPF number (xxx.xxx.xxx-xx): ")
    if validate_cpf(cpf):
        print("The CPF is valid")
    else:
        print("The CPF is invalid")
except ValueError:
    print("Error: The CPF must contain only numbers.")
except Exception as e:
    print(f"Unexpected error: {e}")