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


valor = float(input("Valor do produto: "))

print(Fore.RED + Back.BLACK + "METÓDO DE PAGAMENTO".center(80) + Style.RESET_ALL)
mtd_Pagamento = int(input("1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto.\n"
                          "2 - À Vista no cartão de crédito, recebe 10% de desconto.\n"
                          "3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros.\n"
                          "4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%."))
mtd_Pagamento = mtd_Pagamento - 1

if mtd_Pagamento == 0:
    desconto = valor * 0.15
    newprice = valor - desconto
    print(f"O produto de R$ {valor}, recebeu desconto de 15% R$ {desconto}, agora custa R$ {newprice}")
elif mtd_Pagamento == 1:
    desconto = valor * 0.10
    newprice = valor - desconto
    print(f"O produto de R$ {valor}, recebeu desconto de 10% R$ {desconto}, agora custa R$ {newprice}")
elif mtd_Pagamento == 2:
    print(f"O produto custou R$ {valor}")
elif mtd_Pagamento == 3:
    juros = valor * 0.10
    newprice = valor + juros
    print(f"O produto de R$ {valor}, o juros sera de 10% R$ {juros}, agora custa R$ {newprice}")
else:
    print("Insira o número do modo de pagamento")
