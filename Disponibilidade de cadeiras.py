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

linha = ["A", "B", "C", "D"]

cadeiras = []
busy = []
free = []

def escolha_assento():
    intro = "Olá, Seja Muito Bem Vindo."
    intro2 = "Escolha o Assento Desejado, Ex: (A1, B2, C3...): "
    Cchosed = str(input(Fore.LIGHTYELLOW_EX + Back.BLACK + intro.center(
        60) + Style.RESET_ALL + "\n" + Fore.LIGHTYELLOW_EX + Back.BLACK + intro2.center(
        60) + Style.RESET_ALL + "\nAssentos: ")).strip().capitalize().split(",")
    cadeiras.append(Cchosed)
    print(cadeiras)
    return

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


def mapa():
    countR = 0
    countG = 0
    print(Fore.GREEN + "--" * 30)
    texto = "-- Cinema com filmes --"
    print(Fore.RED + Back.BLACK + texto.center(60) + Style.RESET_ALL)
    print(Fore.GREEN + "--" * 30 + Style.RESET_ALL)
    slot = [Fore.GREEN, Fore.RED]
    for i in linha:
        for num in range(1, 6):
            idt = f"{i}{num}"
            color = random.choice(slot)
            if color == Fore.RED:
                countR += 1
                busy.append(idt)
            else:
                countG += 1
                free.append(idt)
            print(color, idt.center(10), end=" ")
            print(Style.RESET_ALL, end=" ")
        print()

        perctf = (countG / (countR + countG)) * 100
        perctb = (countR / (countR + countG)) * 100
        print(f"Quantidade de Lugares Disponiveis: {slot[0]}{countG}" + Style.RESET_ALL)
        print(f"Cadeiras livres: {slot[0]}{perctf:.0f}%\n{free}\n" + Style.RESET_ALL)
        print(f"Quantidade de Lugares Ocupados: {slot[1]}{countR}" + Style.RESET_ALL)
        print(f"Cadeiras Ocupadas: {slot[1]}{perctb:.0f}%\n{busy}\n" + Style.RESET_ALL)



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
            return
        elif option == 5:
            return
        elif option == 6:
            exit()
            break
        else:
            print(Fore.RED + Back.BLACK + "Opção Invalida, Tente Novamente!" + Style.RESET_ALL)
            continue
        break

    return int(option)


menu()











