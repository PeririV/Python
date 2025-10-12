# 16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é
# equilátero, isósceles ou escaleno.

"""
A = int(input("Insira o valor (em Graus) de A: "))
B = int(input("Insira o valor (em Graus) de B: "))
C = int(input("Insira o valor (em Graus) de C: "))
if A + B + C == 180:
    if A == B and A == C and B == C:
        print("EQUILÀTERO")
    elif A == B and A != C or B == C and A != C:
        print("ISÓCELES")
    elif A != B and A != C and B != C:
        print("ESCALENO")
    else:
        print("Chapa não parceiro")
else:
    print("Chapa não parceiro")

"""
from itertools import count
from os import PRIO_PGRP

"""
#  17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.
# Fórmula: C = (5 * ( F-32) / 9)


Temp = float(input("Insira o valor de Fahrenheit: "))

Celsius = (5 * (Temp - 32) / 9)

print(Celsius)
"""
#18 - Francisco tem 1,50m e cresce 2 centímetros por ano,
# enquanto Sara tem 1,10m e cresce 3 centímetros por ano.
# Faça um algoritmo que calcule e imprima na tela em quantos
# anos serão necessários para que Francisco seja maior que Sara.
"""
Fran = 1.50
Sara = 1.10
Anos = 0

while Fran >= Sara:
    Anos += 1
    Fran += 0.02
    Sara += 0.03
print(f"Serão necessarios {Anos} Anos para que Francisco seja Menor que Sara")
"""

# 19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
"""
Tabuada = 0

while Tabuada <= 9:
    print("TABUADA DO ", Tabuada + 1)
    Tabuada += 1
    Cont = 0

    while Cont <= 9:
            Cont += 1
            Resultado = Tabuada * Cont
            print(f"{Tabuada} * {Cont} = {Resultado}")
"""
"""
# 20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

Tabuada = int(input("Você quer a TAABUADA DO...: "))
Cont = 0
print(f"TABUADA DO {Tabuada}\n")
while Cont <= 9:
    Cont += 1
    resultado = Tabuada * Cont
    print(f"{Tabuada} * {Cont} = {resultado}")
"""

# 21 - Faça um algoritmo que mostre um valor aleatório entre 0 e 100.
"""
import random


print("Jogo da advinhação: ", random.randint(1, 100))
"""

# 22 - Faça um algoritmo que leia dois valores inteiros A e B,
# imprima na tela o quociente e o resto da divisão inteira entre eles.
"""
A = int(input("Primeiro Valor: "))
B = int(input("Segundo Valor: "))

dvsA = A // B
rstA = A % B
print(f"quociente de {A} e {B} = {dvsA}, Resto da divisão de {A} e {B} = {rstA}")

"""

# 23 - Faça um algoritmo que efetue o cálculo do salário líquido de um professor.
# As informações fornecidas serão: valor da hora aula, número de aulas lecionadas
# no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.
"""

SalProf = float(input("Salario R$ "))

ValorH = (SalProf / 21) / 10

if SalProf <= 1518.00:
    Desc = SalProf * 0.075
    SalProf = SalProf - Desc
    print(f"Seu Salario após o desconto de 7,5%  \nR$ {Desc:.2f}, \nR$ {SalProf:.2f} \nValor Hora R$ {ValorH:.2f} com 21 dias trabalhados")

elif SalProf >= 1518.01 and SalProf <= 2793.88:
    Desc = SalProf * 0.09
    SalProf = SalProf - Desc
    print(f"Seu Salario após o desconto de 9%  \nR$ {Desc:.2f},  \nR$ {SalProf:.2f} \nValor Hora R$ {ValorH:.2f} com 21 dias trabalhados")

elif SalProf >= 2793.89 and SalProf <= 4190.83:
    Desc = SalProf * 0.12
    SalProf = SalProf - Desc
    print(f"Seu Salario após o desconto de 12% \nR$ {Desc:.2f}, \nR$ {SalProf:.2f} \nValor Hora R$ {ValorH:.2f} com 21 dias trabalhados")

elif SalProf >= 4190.84 and SalProf <= 8157.41:
    Desc = SalProf * 0.14
    SalProf = SalProf - Desc
    print(f"Seu Salario após o desconto de 14%  \nR$ {Desc:.2f}, \nR$ {SalProf:.2f} \nValor Hora R$ {ValorH:.2f} com 21 dias trabalhados")

else:
    Desc = SalProf * 0.14
    SalProf = SalProf - Desc
    print(f"Me contrata como assistente, tu ta cheio da grana\nDesconto de 14% {Desc:.2f} \n R$ {SalProf:.2f}\nValor Hora R$ {ValorH:.2f}")

"""


#22 - Faça um algoritmo que calcule a quantidade de litros de combustível
# gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se
# fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média,
# distância percorrida e a quantidade de litros utilizados para fazer a viagem.
# Fórmula: distância = tempo x velocidade.
#           litros usados = distância / 12.

Km = 12
Distancia = int(input("Distancia Km "))
veloMedia = int(input("Velocidade média Km "))
tempo =  Distancia / veloMedia
litros = Distancia / Km

print(f"Litros gastos com a viagem L {litros:.2f}\nTempo de viagem {tempo:.2f} Horas")