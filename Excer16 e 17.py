# 16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é
# equilátero, isósceles ou escaleno.

"""
A = int(input("Insira o valor (em Graus) de A: "))
B = int(input("Insira o valor (em Graus) de B: "))
C = int(input("Insira o valor (em Graus) de C: "))


if A == B and A == C and B == C:
    print("EQUILÀTERO")
elif A == B and A != C or B == C and A != C:
    print("ISÓCELES")
elif A != B and A != C and B != C:
    print("ESCALENO")
else:
    print("Chapa não parceiro")

"""




#  17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.
# Fórmula: C = (5 * ( F-32) / 9)


Temp = float(input("Insira o valor de Fahrenheit: "))

Celsius = (5 * (Temp - 32) / 9)

print(Celsius)