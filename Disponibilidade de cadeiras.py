# Represente uma sala de cinema com 4 fileiras (A-D) e 5 cadeiras por fileira
# Inicialize com algumas cadeiras já ocupadas aleatoriamente
# Mostre o mapa visual da sala
# Liste todas as cadeiras disponíveis
# Liste todas as cadeiras indisponíveis
# Calcule e mostre estatísticas totais"

linha = ["A", "B", "C", "D"]

for i in linha:
    for num in range(1,6):
        print(f"{i}-{num}")
