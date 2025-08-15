# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#1 - Faça um algoritmo que leia os valores de A, B, C e
# em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

#2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número
# é par ou ímpar, positivo ou negativo.

#3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B
# forem iguais, deverá somar os dois valores,


def tudovezes():
    vezes = Valor1 * Valor2
    Valor3 = vezes
    print(f"Valor C Foi substituido para: {Valor3}, A * B")


def imparpar():
    if Soma % 2 == 0:
        print("A Soma é: Par")
    else:
        print("A Soma é: Impar")


Valor1 =  int(input("Insira o primeiro valor: "))
Valor2 =  int(input("Insira o segundo valor: "))
Valor3 = int(input("Insira o terceiro valor: "))

print(f"\n \nValor A: {Valor1},\nValor B: {Valor2},\nValor C: {Valor3}.")

Soma = Valor1 + Valor2

if Valor1 == Valor2:
    if Soma < Valor3:
        print(f"O Terceiro (C) Valor {Valor3} é maior que {Soma}")
        imparpar()
    elif Soma > Valor3:
        print(f"A Soma dos Valores A e B {Soma} resulta em um numero maior que o Terceiro (C) {Valor3}")
        imparpar()
    else:
        print(f"A soma dos valores A e B {Soma} se igualam ao (C) {Valor3}")
        imparpar()
else:
    print("Os Valores A e B NÃO SÃO IDENTICOS")
    tudovezes()

