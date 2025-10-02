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

from datetime import date
from colorama import Fore, Back, Style


def calcular_idade_detalhada(data_nascimento):
    """Calcula idade em anos, meses e dias"""
    hoje = date.today()

    anos = hoje.year - data_nascimento.year
    meses = hoje.month - data_nascimento.month
    dias = hoje.day - data_nascimento.day

    # Ajuste para dias negativos
    if dias < 0:
        meses -= 1
        # Dias no mês anterior
        if hoje.month == 1:
            dias_prev_mes = 31  # Dezembro tem 31 dias
        else:
            dias_prev_mes = (date(hoje.year, hoje.month, 1) - date(hoje.year, hoje.month - 1, 1)).days
        dias = dias_prev_mes + dias

    # Ajuste para meses negativos
    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias


try:
    print(Fore.RED + Back.BLACK + "Formato (DD/MM/AAAA)" + Style.RESET_ALL)
    nasc_input = input("Data de nascimento: ").split("/")

    if len(nasc_input) != 3:
        print("Formato inválido! Use DD/MM/AAAA")
        exit()

    dia = int(nasc_input[0])
    mes = int(nasc_input[1])
    ano = int(nasc_input[2])

    # Validação da data
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0):
        print("Data inválida!")
        exit()

    # Cria objeto date para validação adicional
    data_nasc = date(ano, mes, dia)
    hoje = date.today()

    if data_nasc > hoje:
        print("Data de nascimento não pode ser no futuro!")
        exit()

    # Calcula idade detalhada
    anos, meses, dias = calcular_idade_detalhada(data_nasc)

    print(f"\n{Fore.GREEN}Você viveu:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{anos} anos, {meses} meses e {dias} dias{Style.RESET_ALL}")

except ValueError as e:
    print(f"Erro: Data inválida! Certifique-se de usar números válidos.")
except Exception as e:
    print(f"Erro inesperado: {e}")