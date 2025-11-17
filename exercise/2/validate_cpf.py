# Validate CPF input.

# This script checks that a CPF (Brazilian taxpayer ID) entered by the user
# contains exactly 11 numeric digits. If the input contains letters or any
# non-numeric characters, or does not have 11 digits, an error message is shown.


def validate_cpf(cpf):
    if not cpf.isdigit():
        return "Error: CPF must contain only numbers."
    if len(cpf) != 11:
        return "Error: CPF must have exactly 11 digits."
    return "Valid CPF."


cpf = input("Enter your CPF: ")
print(validate_cpf(cpf))