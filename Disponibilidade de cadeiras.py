# Represente uma sala de cinema com 4 fileiras (A-D) e 5 cadeiras por fileira
# Inicialize com algumas cadeiras já ocupadas aleatoriamente
# Mostre o mapa visual da sala
# Liste todas as cadeiras disponíveis
# Liste todas as cadeiras indisponíveis
# Calcule e mostre estatísticas totais"
import random

from colorama import Fore, Back, Style
import random
linha = ["A", "B", "C", "D"]

#for i in linha:
#    for num in range(1,6):
#        print(f"{i}-{num}")
print(Fore.GREEN + "--" * 30)
texto = "-- Cinema com filmes --"
print(Fore.RED + Back.BLACK + texto.center(60) + Style.RESET_ALL)
print(Fore.GREEN + "--" * 30 + Style.RESET_ALL)
slot = [Fore.GREEN , Fore.RED ]

for i in linha:
    for num in range(1,6):
        idt = f"{i}{num}"
        color = random.choice(slot)
        print(color)
        print(idt.center(12), end=" ")
        print(Style.RESET_ALL, end=" ")
    print()
