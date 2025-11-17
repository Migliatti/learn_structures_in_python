# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada.

import random

def guess_number():
    try:
        number_to_guess = random.randint(1, 100)
        while True:
            user_input = int(input("Adivinhe o número entre 1 e 100: "))
            if user_input < 1 or user_input > 100:
                raise ValueError("O número deve estar entre 1 e 100.")
            if user_input < number_to_guess:
                print("Está abaixo do número correto. Tente novamente.")
            elif user_input > number_to_guess:
                print("Está acima do número correto. Tente novamente.")
            else:
                print("Parabéns! Você acertou o número.")
                break
    except ValueError as ve:
        print(f"Entrada inválida: {ve}. Por favor, tente novamente.")
        guess_number()

guess_number()