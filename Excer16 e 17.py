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

Tabuada = 0

while Tabuada <= 9:
    print("TABUADA DO ", Tabuada + 1)
    Tabuada += 1
    Cont = 0

    while Cont <= 9:
            Cont += 1
            Resultado = Tabuada * Cont
            print(f"{Tabuada} * {Cont} = {Resultado}")