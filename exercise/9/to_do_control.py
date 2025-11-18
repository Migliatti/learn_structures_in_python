# Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

# Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

# fazer um menu com opções de adicionar, visualizar e remover tarefas
import os

def menu():
    while True:
        try:
            os.system('cls')
            print(''' 
▄▄▄█████▓ ▒█████  ▓█████▄  ▒█████      ██▓     ██▓  ██████ ▄▄▄█████▓
▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ██▌▒██▒  ██▒   ▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒
▒ ▓██░ ▒░▒██░  ██▒░██   █▌▒██░  ██▒   ▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
░ ▓██▓ ░ ▒██   ██░░▓█▄   ▌▒██   ██░   ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ 
  ▒██▒ ░ ░ ████▓▒░░▒████▓ ░ ████▓▒░   ░██████▒░██░▒██████▒▒  ▒██▒ ░ 
  ▒ ░░   ░ ▒░▒░▒░  ▒▒▓  ▒ ░ ▒░▒░▒░    ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   
    ░      ░ ▒ ▒░  ░ ▒  ▒   ░ ▒ ▒░    ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    
  ░      ░ ░ ░ ▒   ░ ░  ░ ░ ░ ░ ▒       ░ ░    ▒ ░░  ░  ░    ░      
             ░ ░     ░        ░ ░         ░  ░ ░        ░           
                   ░                                                
        ''')
            print("1. Add a task")
            print("2. Visualize task(s)")
            print("3. Remove task")
            print("4. Exit App")
            choice = int(input("\nSelect what you want to do: "))

            match choice:
                case 1:
                    print("Choose - 1")
                    input("Press ENTER to continue")
                case 2:
                    print("Choose - 2")
                    input("Press ENTER to continue")
                case 3:
                    print("Choose - 3")
                    input("Press ENTER to continue")
                case 4:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid Value, try again")
                    input("Press ENTER to continue")
        except ValueError:
            print("Invalid Value, try again.")
            input("Press ENTER to continue.")

menu()
