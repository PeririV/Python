#  13 - Faça algoritmo que leia o nome e a idade de uma pessoa e imprima
#  na tela o nome da pessoa e se ela é maior ou menor de idade.


try:
    Nome = str(input("Insira o seu Nome: "))
    idade = -1
    print(f"Olã {Nome}, Poderia me dizer sua idade?")

    while idade < 0:
        try:
            idade = int(input("\nInsira a sua idade: "))
            if idade <= 0:
                print("Insira apenas números")


        except ValueError:
            print("Insira apenas números")
            idade = -1

    if idade <= 10:
        print(f"\nOpa {Nome}, Caramba!!! {idade} anos, OH AI SIM HEIN\nVocê já é um Garotão")

    elif idade <= 17 :
        print(f"\nOpa {Nome}, Caramba!!! {idade} anos, OH AI SIM HEIN\nVocê já é um Adolecente")

    elif idade <= 45:
        print(f"\nOpa {Nome}, Caramba!!! {idade} anos, OH AI SIM HEIN\nVocê já é um Adulto")
    else:
        print("\nMas senhor, que isso, quer tomar um chá!?")

except ValueError:
    print("\nErro inesperado, Tente novamente")


