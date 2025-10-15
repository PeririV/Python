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

print(Fore.GREEN + "--" * 30)
texto = "-- Cinema com filmes --"
print(Fore.RED + Back.BLACK + texto.center(60) + Style.RESET_ALL)
print(Fore.GREEN + "--" * 30 + Style.RESET_ALL)
slot = [Fore.GREEN , Fore.RED ]
countR = 0
countG = 0
busy = []
free = []

for i in linha:
    for num in range(1,6):
        idt = f"{i}{num}"
        color = random.choice(slot)
        if color == Fore.RED:
            countR += 1
            busy.append(idt)
        else:
            countG += 1
            free.append(idt)
        print(color, idt.center(10), end=" ")
        print(Style.RESET_ALL, end=" ")
    print()

print(f"Quantidade de Lugares Disponiveis: {slot[0]}{countG}" + Style.RESET_ALL)
print(f"Cadeiras livres: \n{free}")
print(f"Quantidade de Lugares Ocupados: {slot[1]}{countR}" + Style.RESET_ALL)
print(f"Cadeiras Ocupadas: \n{busy}")

