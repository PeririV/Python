# 14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A
# por B e o valor de B por A e imprima na tela os valores.
"""
A = 0
B = 0

Aa = int(input("Valor A: "))
Bb = int(input("Valor B: "))

A = Bb
B = Aa
print(f"Os valores de A: {Aa} e B: {Bb}")

print(f"Agora A: {A} e B: {B}")
"""

# 15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na
# tela quantos anos, meses e dias essa pessoa ja viveu. Leve em
# consideração o ano com 365 dias e o mês com 30 dias.
# (Ex: 5 anos, 2 meses e 15 dias de vida)

from datetime import datetime
from colorama import Fore, Back, Style

hoje = datetime.now()

try:
    print(Fore.RED + Back.BLACK + "Formato (11/10/1999)" + Style.RESET_ALL)
    Nasc = input("Data de nascimento: ").split("/")
    print(Nasc)

    dia = int(Nasc[0])
    mes = int(Nasc[1])
    ano = int(Nasc[2])

    if len(Nasc) != 3:
        print("Formato Invalido")

    if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
        print(dia, mes, ano)
        hoje.day()
    else:
        print("Data inválida!")
except ValueError:
    print("Erro: Digite números válidos!")
