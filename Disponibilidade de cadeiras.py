# Represente uma sala de cinema com 4 fileiras (A-D) e 5 cadeiras por fileira
# Inicialize com algumas cadeiras já ocupadas aleatoriamente
# Mostre o mapa visual da sala
# Liste todas as cadeiras disponíveis
# Liste todas as cadeiras indisponíveis
# Calcule e mostre estatísticas totais"
 ########################################
# Use dicionários para armazenar o estado das cadeiras
# Valide sempre as entradas do usuário
# Trate erros com try/except
# Modularize em funções pequenas e específicas
# Use list comprehension para filtrar cadeiras
#  DESAFIO BÔNUS:
# Crie um sistema onde o usuário pode:
# Ver mapa colorido
# Reservar múltiplas cadeiras
# Cancelar reservas
# Ver histórico de operações
# Salvar/recuperar estado
from itertools import count

from colorama import Fore, Back, Style
import random

cadeiras = []
busy = []
free = []

def retornar_menu():
    escolha = int(input("1 - Retornar ao Menu Principal\n2- Sair\nSua Escolha: "))
    if escolha == 1:
        menu()
    else:
        exit()

def escolha_assento():
    intro = "Olá, Seja Muito Bem Vindo."
    intro2 = "Escolha o Assento Desejado, Ex: (A1, B2, C3...): "
    Cchosed = str(input(Fore.LIGHTYELLOW_EX + Back.BLACK + intro.center(
        60) + Style.RESET_ALL + "\n" + Fore.LIGHTYELLOW_EX + Back.BLACK + intro2.center(
        60) + Style.RESET_ALL + "\nAssentos: ")).strip().capitalize().split(",")
    cadeiras.append(Cchosed)
    print(cadeiras)
    retornar_menu()

def exit():
    print(Fore.BLACK + Back.RED + "Saindo do sistema..." + Style.RESET_ALL)


def cancelar_assento():
    intro = "Qual Assento Gostaria de Remover? "
    intro2 = "..." * 15
    Cchosed = str(input(Fore.LIGHTYELLOW_EX + Back.BLACK + intro.center(
        60) + Style.RESET_ALL + "\n" + Fore.LIGHTYELLOW_EX + Back.BLACK + intro2.center(
        60) + Style.RESET_ALL + "\nAssentos: " )).strip().capitalize().split(",")
    if not cadeiras:
        print("Não há Assentos Para Cancelar")
        return menu()
    else:
        cadeiras.remove(Cchosed)

    print("Assentos Atuais", cadeiras)
    retornar_menu()

def Assentos_Disp():
    if not free:
        print(f"{Fore.YELLOW}Não há cadeiras disponíveis no momento.{Style.RESET_ALL}")
        return

    print("\n" + "-" * 40)
    print(f"{Fore.GREEN}CADEIRAS DISPONÍVEIS{Style.RESET_ALL}".center(40))
    print("-" * 40)

    print(f"{Fore.GREEN}Cadeiras livres: {len(free)} cadeira(s){Style.RESET_ALL}")
    print("Cadeiras:", ", ".join(free))

    # Mostrar em formato de grid
    print("\nMapa de Assentos Disponíveis:")
    linha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in linha:
        for num in range(1, 6):
            idt = f"{i}{num}"
            if idt in free:
                print(f"{Fore.GREEN}{idt.center(5)}{Style.RESET_ALL}", end=" ")
            else:
                print(f"{Fore.RED}{idt.center(5)}{Style.RESET_ALL}", end=" ")
        print()
        retornar_menu()


def estastistica():
    if not free and not busy:
        print("Nenhum dado disponível para estatísticas.")
        return

    total_cadeiras = len(free) + len(busy)

    if total_cadeiras > 0:
        perct_livres = (len(free) / total_cadeiras) * 100
        perct_ocupadas = (len(busy) / total_cadeiras) * 100
    else:
        perct_livres = 0
        perct_ocupadas = 0

    print("\n" + "=" * 50)
    print("ESTATÍSTICAS DO CINEMA".center(50))
    print("=" * 50)

    print(f"{Fore.GREEN}Cadeiras Livres: {len(free)} ({perct_livres:.1f}%){Style.RESET_ALL}")
    print(f"Cadeiras livres: {free}")

    print(f"{Fore.RED}Cadeiras Ocupadas: {len(busy)} ({perct_ocupadas:.1f}%){Style.RESET_ALL}")
    print(f"Cadeiras ocupadas: {busy}")

    print(f"Total de cadeiras: {total_cadeiras}")
    print("=" * 50)

def mapa():
    global free, busy
    free = []
    busy = []

    print("\n" + Fore.GREEN + "==" * 30)
    texto = "CINEMA - MAPA COMPLETO"
    print(Fore.RED + Back.BLACK + texto.center(60) + Style.RESET_ALL)
    print(Fore.GREEN + "==" * 30 + Style.RESET_ALL)

    # Cabeçalho da tela
    print(f"{Fore.CYAN}TELA{Style.RESET_ALL}".center(60))
    print(f"{Fore.CYAN}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■{Style.RESET_ALL}".center(60))
    print()

    # Legendas
    print(f"{Fore.GREEN}□ Disponível{Style.RESET_ALL} | {Fore.RED}■ Ocupado{Style.RESET_ALL}")
    print()

    linha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    slot = [Fore.GREEN, Fore.RED]

    # Mapa das cadeiras
    for i in linha:
        print(f"Fileira {i}: ", end="")
        for num in range(1, 11):
            idt = f"{i}{num}"
            color = random.choice(slot)

            if color == Fore.RED:
                busy.append(idt)
            else:
                free.append(idt)

            # Usar símbolos visuais
            simbolo = "■" if color == Fore.RED else "□"
            print(color + simbolo + Style.RESET_ALL, end="  ")
        print()  # Nova linha para próxima fileira

    # Estatísticas após gerar o mapa
    total_cadeiras = len(free) + len(busy)
    if total_cadeiras > 0:
        perct_livres = (len(free) / total_cadeiras) * 100
        perct_ocupadas = (len(busy) / total_cadeiras) * 100
    else:
        perct_livres = 0
        perct_ocupadas = 0

    print(f"\n{Fore.GREEN}Lugares Disponíveis: {len(free)} ({perct_livres:.1f}%){Style.RESET_ALL}")
    print(f"{Fore.RED}Lugares Ocupados: {len(busy)} ({perct_ocupadas:.1f}%){Style.RESET_ALL}")
    retornar_menu()

def menu():
    while True:
        print(Fore.GREEN + "--" * 30 + Style.RESET_ALL)
        texto = "-- MENU DO CINEMA --"
        print(Fore.RED + Back.BLACK + texto.center(60) + Style.RESET_ALL)
        print(Fore.GREEN + "--" * 30 + Style.RESET_ALL)

        # Menu options
        print("Selecione uma das opções abaixo:")
        print("1 - Ver Mapa Das Cadeiras")
        print("2 - Escolher Assentos")
        print("3 - Cancelar Assentos")
        print("4 - Assentos Disponiveis")
        print("5 - Estastiticas Dos Assentos")
        print("6 - Sair")

        # Input with styling
        option = int(input(Fore.LIGHTYELLOW_EX + Back.BLACK + "Escolha: " + Style.RESET_ALL))
        print(f"Você selecionou a opção: {option}")

        try:
            option_int = int(option)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if option == 1:
            mapa()
            return

        elif option == 2:
            escolha_assento()
        elif option == 3:
            cancelar_assento()
        elif option == 4:
            Assentos_Disp()
        elif option == 5:
            estastistica()
        elif option == 6:
            exit()
            break
        else:
            print(Fore.RED + Back.BLACK + "Opção Invalida, Tente Novamente!" + Style.RESET_ALL)
            continue
        break

    return int(option)


menu()











