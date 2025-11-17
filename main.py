import random

def somar(numero1, numero2):
    return numero1 + numero2

try:
    numero1 = float(random.randint(0, 100))
    numero2 = float(random.randint(0, 100))
    resultado = somar(numero1, numero2)
    print(f"O resultado da soma de {numero1} e {numero2} é {resultado}")
except ValueError:
    print("Erro: Os valores devem ser números válidos.")
except Exception as e:
    print(f"Erro inesperado: {e}")