import math

# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

# Valor1 =  int(input("Insira o primeiro valor: "))

# print(f"Seu Valor: {Valor1}, \nO Antecessor: {Valor1 - 1}, \nO Sucessor: {Valor1 + 1}")


# 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um
# usuário, calcule quantos salários mínimos esse
# usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

import math

#SalMin = float(1293.20)
#SalMinUser = float(input("Insira seu salário: "))
#bonus = SalMinUser + (SalMinUser * 0.05)
#mediaSal = SalMinUser / SalMin
#print(f"Salario do Usuario: R$ {SalMinUser:.2f} "
#      f"\nMédia de {mediaSal:.2f} Vezes o Salário Minimo")
#print(f"Você Recebeu um bonus de 5% do seu salário, Agora você recebe: {bonus}")

# 7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e
# determine se ambos são VERDADEIRO ou FALSO.

#Value1 = input("1 - Insira true OU false: ").lower() == "true"
#Value2 = input("2 - Insira true OU false: ").lower() == "true"

#if Value1 and Value2:
#    print("Ambos são verdadeiros -- iguais")
#elif not Value1 and not Value2:
#    print("Os dois são falsos -- iguais")
#else:
#    print("Não corresponde")

# 8 - Faça um algoritmo que leia três valores inteiros diferentes e
# imprima na tela os valores em ordem decrescente.

#A = int(input("Insira um valor ( 0 a 10 ): "))
#B = int(input("Insira um valor ( 0 a 10 ): "))
#C = int(input("Insira um valor ( 0 a 10 ): "))
#ordenados_desc = sorted([A,B,C], reverse= True)
#print(ordenados_desc)

# 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o s
# eu peso e sua altura e imprima na tela sua condição
# de acordo com a tabela abaixo:
# Fórmula do IMC = peso / (altura) ²
# Tabela Condições IMC
#
#  Abaixo de 18,5   | Abaixo do peso
#  Entre 18,6 e 24,9 | Peso ideal (parabéns)
#  Entre 25,0 e 29,9 | Levemente acima do peso
#  Entre 30,0 e 34,9 | Obesidade grau I
#  Entre 35,0 e 39,9 | Obesidade grau II (severa)
#  Maior ou igual a 40 | Obesidade grau III (mórbida)

"""peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

IMC = peso / (altura ** 2)


if IMC <= float("18.5"):
    print("Abaixo do peso")
elif IMC >= float("18.6") and IMC <= float("24.9"):
    print("Peso Ideal (PARABENS!!!)")
elif IMC <= float("29.9") and IMC >= float("25.0"):
    print("Levemente acima do peso")
elif IMC <= float("34.9") and IMC >= float("30.0"):
    print("Obesidade grau I")
elif IMC <= float("39.9") and IMC >= float("35.0"):
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida)\nCALMA AI AMIGÃO")
print(IMC)
"""

#  10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.


