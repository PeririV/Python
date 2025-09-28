# 12 - Faça um algoritmo que leia o valor de um produto e determine o
# valor que deve ser pago, conforme a escolha da forma de pagamento
#  pelo comprador e imprima na tela o valor final do produto a ser pago.
#  Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
#
#  Tabela de Código de Condições de Pagamento
#
#  1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
#  2 - À Vista no cartão de crédito, recebe 10% de desconto
#  3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
#  4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
from idlelib.multicall import MC_ENTER
from colorama import Fore, Back, Style
import os
# Limpar tela (opcional)
os.system('cls' if os.name == 'nt' else 'clear')


try:
    opc = [1, 2, 3, 4]
    mtd_Pagamento = 0

    valor = float(input("Valor do produto: "))
    while mtd_Pagamento not in opc:
        print(Fore.RED + Back.BLACK + "METÓDO DE PAGAMENTO ( 1 - 4 )".center(80) + Style.RESET_ALL)
        print("1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto.\n"
                                  "2 - À Vista no cartão de crédito, recebe 10% de desconto.\n"
                                  "3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros.\n"
                                  "4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%.")

        try:
            mtd_Pagamento = int(input("Insira a forma de pagamento: "))
            if mtd_Pagamento not in opc:
                print(Fore.RED + "\n❌ Opção inválida! Digite um número entre 1 e 4." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "\n❌ Erro! Digite apenas números." + Style.RESET_ALL)
            mtd_Pagamento = 0

    if mtd_Pagamento == 1:
        desconto = valor * 0.15
        newprice = valor - desconto
        print(f"O produto de R$ {valor}, recebeu desconto de 15% R$ {desconto}, agora custa R$ {newprice}")
    elif mtd_Pagamento == 2:
        desconto = valor * 0.10
        newprice = valor - desconto
        print(f"O produto de R$ {valor}, recebeu desconto de 10% R$ {desconto}, agora custa R$ {newprice}")
    elif mtd_Pagamento == 3:
        print(f"O produto custou R$ {valor}")
    elif mtd_Pagamento == 4:
        juros = valor * 0.10
        newprice = valor + juros
        print(f"O produto de R$ {valor}, o juros sera de 10% R$ {juros}, agora custa R$ {newprice}")
    else:
        print("Tente Novamente, Escolha a Forma de Pagamento")
except ValueError:
    print(Fore.RED +"\nTente Novamente, Insira o Valor do produto!" + Style.RESET_ALL)
except KeyboardInterrupt:
    print(Fore.YELLOW + "\n\nPrograma interrompido pelo usuário." + Style.RESET_ALL)
except Exception as e:
    print(Fore.RED + f"\n❌ Erro inesperado: {e}" + Style.RESET_ALL)
print(Fore.CYAN + "\nObrigado por usar nosso sistema! 🛒" + Style.RESET_ALL)

