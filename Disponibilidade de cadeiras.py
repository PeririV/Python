# Represente uma sala de cinema com 4 fileiras (A-D) e 5 cadeiras por fileira
# Inicialize com algumas cadeiras já ocupadas aleatoriamente
# Mostre o mapa visual da sala
# Liste todas as cadeiras disponíveis
# Liste todas as cadeiras indisponíveis
# Calcule e mostre estatísticas totais"
 ########################################
# Use dicionários para armazenar o estado das cadeiras
# Valide sempre as entradas do usuário
# Trate erros com try/except
# Modularize em funções pequenas e específicas
# Use list comprehension para filtrar cadeiras
#  DESAFIO BÔNUS:
# Crie um sistema onde o usuário pode:
# Ver mapa colorido
# Reservar múltiplas cadeiras
# Cancelar reservas
# Ver histórico de operações
# Salvar/recuperar estado

from colorama import Fore, Back, Style
import random
import json
from datetime import datetime


class Cinema:
    def __init__(self):
        self.fileiras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.cadeiras_por_fileira = 10
        self.estado_cadeiras = {}  # 'A1': True (ocupada), False (livre)
        self.historico = []
        self.cor_livre = Fore.GREEN
        self.cor_ocupada = Fore.RED
        self.arquivo_estado = "estado_cinema.json"
        self.inicializar_sala()

    def inicializar_sala(self):
        """Inicializa a sala com algumas cadeiras ocupadas aleatoriamente"""
        for fileira in self.fileiras:
            for numero in range(1, self.cadeiras_por_fileira + 1):
                cadeira_id = f"{fileira}{numero}"
                # 30% de chance de estar ocupada inicialmente
                self.estado_cadeiras[cadeira_id] = random.random() < 0.3

        self.registrar_operacao("Sistema", "Sala inicializada")

    def obter_cadeiras_livres(self):
        """Retorna lista de cadeiras livres usando list comprehension"""
        return [cadeira for cadeira, ocupada in self.estado_cadeiras.items() if not ocupada]

    def obter_cadeiras_ocupadas(self):
        """Retorna lista de cadeiras ocupadas usando list comprehension"""
        return [cadeira for cadeira, ocupada in self.estado_cadeiras.items() if ocupada]

    def validar_cadeira(self, cadeira):
        """Valida se o formato da cadeira é válido"""
        if len(cadeira) < 2:
            return False

        fileira = cadeira[0].upper()
        try:
            numero = int(cadeira[1:])
            return fileira in self.fileiras and 1 <= numero <= self.cadeiras_por_fileira
        except ValueError:
            return False

    def registrar_operacao(self, usuario, operacao):
        """Registra operação no histórico"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historico.append({
            'timestamp': timestamp,
            'usuario': usuario,
            'operacao': operacao
        })

    def mostrar_mapa_colorido(self):
        """Mostra mapa visual colorido da sala"""
        print(f"\n{Fore.CYAN}{'MAPAS DA SALA DE CINEMA':^40}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")

        # Cabeçalho da tela
        print(f"\n{Fore.CYAN}{' ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ':*^40}{Style.RESET_ALL}\n")

        # Legendas
        print(f"{self.cor_livre}□ Disponível{Style.RESET_ALL} | {self.cor_ocupada}■ Ocupado{Style.RESET_ALL}\n")

        # Mapa das cadeiras
        print("   " + "".join(f"{i:^3}" for i in range(1, self.cadeiras_por_fileira + 1)))

        for fileira in self.fileiras:
            print(f"{fileira} |", end=" ")
            for numero in range(1, self.cadeiras_por_fileira + 1):
                cadeira_id = f"{fileira}{numero}"
                if self.estado_cadeiras[cadeira_id]:
                    simbolo = f"{self.cor_ocupada}■{Style.RESET_ALL}"
                else:
                    simbolo = f"{self.cor_livre}□{Style.RESET_ALL}"
                print(simbolo, end="  ")
            print()

    def reservar_cadeiras(self, usuario):
        """Permite reservar múltiplas cadeiras"""
        cadeiras_livres = self.obter_cadeiras_livres()

        if not cadeiras_livres:
            print(f"{Fore.RED}Não há cadeiras disponíveis para reserva.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.GREEN}Cadeiras disponíveis: {', '.join(cadeiras_livres)}{Style.RESET_ALL}")

        try:
            entrada = input("Digite as cadeiras para reservar (ex: A1,B2,C3): ").strip()
            cadeiras_selecionadas = [cadeira.strip().upper() for cadeira in entrada.split(',')]

            cadeiras_validas = []
            cadeiras_invalidas = []

            for cadeira in cadeiras_selecionadas:
                if self.validar_cadeira(cadeira):
                    if not self.estado_cadeiras[cadeira]:
                        cadeiras_validas.append(cadeira)
                    else:
                        print(f"{Fore.RED}Cadeira {cadeira} já está ocupada.{Style.RESET_ALL}")
                else:
                    cadeiras_invalidas.append(cadeira)

            if cadeiras_invalidas:
                print(f"{Fore.RED}Cadeiras inválidas: {', '.join(cadeiras_invalidas)}{Style.RESET_ALL}")

            if cadeiras_validas:
                for cadeira in cadeiras_validas:
                    self.estado_cadeiras[cadeira] = True

                operacao = f"Reserva: {', '.join(cadeiras_validas)}"
                self.registrar_operacao(usuario, operacao)
                print(f"{Fore.GREEN}Reserva confirmada para: {', '.join(cadeiras_validas)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Nenhuma cadeira válida foi selecionada.{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}Erro ao processar reserva: {e}{Style.RESET_ALL}")

    def cancelar_reservas(self, usuario):
        """Permite cancelar reservas de múltiplas cadeiras"""
        cadeiras_ocupadas = self.obter_cadeiras_ocupadas()

        if not cadeiras_ocupadas:
            print(f"{Fore.YELLOW}Não há cadeiras ocupadas para cancelar.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.RED}Cadeiras ocupadas: {', '.join(cadeiras_ocupadas)}{Style.RESET_ALL}")

        try:
            entrada = input("Digite as cadeiras para cancelar (ex: A1,B2,C3): ").strip()
            cadeiras_selecionadas = [cadeira.strip().upper() for cadeira in entrada.split(',')]

            cadeiras_validas = []
            cadeiras_invalidas = []

            for cadeira in cadeiras_selecionadas:
                if self.validar_cadeira(cadeira):
                    if self.estado_cadeiras[cadeira]:
                        cadeiras_validas.append(cadeira)
                    else:
                        print(f"{Fore.YELLOW}Cadeira {cadeira} já está livre.{Style.RESET_ALL}")
                else:
                    cadeiras_invalidas.append(cadeira)

            if cadeiras_invalidas:
                print(f"{Fore.RED}Cadeiras inválidas: {', '.join(cadeiras_invalidas)}{Style.RESET_ALL}")

            if cadeiras_validas:
                for cadeira in cadeiras_validas:
                    self.estado_cadeiras[cadeira] = False

                operacao = f"Cancelamento: {', '.join(cadeiras_validas)}"
                self.registrar_operacao(usuario, operacao)
                print(f"{Fore.GREEN}Cancelamento confirmado para: {', '.join(cadeiras_validas)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Nenhuma cadeira válida foi selecionada.{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}Erro ao processar cancelamento: {e}{Style.RESET_ALL}")

    def listar_cadeiras_disponiveis(self):
        """Lista todas as cadeiras disponíveis"""
        cadeiras_livres = self.obter_cadeiras_livres()

        print(f"\n{Fore.GREEN}{'CADEIRAS DISPONÍVEIS':^40}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'=' * 40}{Style.RESET_ALL}")

        if cadeiras_livres:
            print(f"Total: {len(cadeiras_livres)} cadeira(s)")
            print("Cadeiras:", ", ".join(cadeiras_livres))

            # Mostrar em formato de grid
            print("\nMapa de Disponíveis:")
            for fileira in self.fileiras:
                for numero in range(1, self.cadeiras_por_fileira + 1):
                    cadeira_id = f"{fileira}{numero}"
                    if cadeira_id in cadeiras_livres:
                        print(f"{self.cor_livre}{cadeira_id:^5}{Style.RESET_ALL}", end=" ")
                    else:
                        print(f"{' ':^5}", end=" ")
                print()
        else:
            print(f"{Fore.YELLOW}Não há cadeiras disponíveis.{Style.RESET_ALL}")

    def listar_cadeiras_indisponiveis(self):
        """Lista todas as cadeiras indisponíveis"""
        cadeiras_ocupadas = self.obter_cadeiras_ocupadas()

        print(f"\n{Fore.RED}{'CADEIRAS INDISPONÍVEIS':^40}{Style.RESET_ALL}")
        print(f"{Fore.RED}{'=' * 40}{Style.RESET_ALL}")

        if cadeiras_ocupadas:
            print(f"Total: {len(cadeiras_ocupadas)} cadeira(s)")
            print("Cadeiras:", ", ".join(cadeiras_ocupadas))
        else:
            print(f"{Fore.GREEN}Todas as cadeiras estão disponíveis!{Style.RESET_ALL}")

    def mostrar_estatisticas(self):
        """Calcula e mostra estatísticas totais"""
        total_cadeiras = len(self.estado_cadeiras)
        cadeiras_livres = len(self.obter_cadeiras_livres())
        cadeiras_ocupadas = len(self.obter_cadeiras_ocupadas())

        if total_cadeiras > 0:
            percentual_livres = (cadeiras_livres / total_cadeiras) * 100
            percentual_ocupadas = (cadeiras_ocupadas / total_cadeiras) * 100
        else:
            percentual_livres = percentual_ocupadas = 0

        print(f"\n{Fore.CYAN}{'ESTATÍSTICAS DO CINEMA':^50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

        print(f"{Fore.GREEN}Cadeiras Livres: {cadeiras_livres} ({percentual_livres:.1f}%){Style.RESET_ALL}")
        print(f"{Fore.RED}Cadeiras Ocupadas: {cadeiras_ocupadas} ({percentual_ocupadas:.1f}%){Style.RESET_ALL}")
        print(f"Total de Cadeiras: {total_cadeiras}")
        print(f"Fileiras: {', '.join(self.fileiras)}")
        print(f"Cadeiras por fileira: {self.cadeiras_por_fileira}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

    def mostrar_historico(self):
        """Mostra o histórico de operações"""
        print(f"\n{Fore.MAGENTA}{'HISTÓRICO DE OPERAÇÕES':^60}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'=' * 60}{Style.RESET_ALL}")

        if not self.historico:
            print(f"{Fore.YELLOW}Nenhuma operação registrada.{Style.RESET_ALL}")
            return

        for operacao in self.historico[-10:]:  # Mostrar últimas 10 operações
            print(f"{operacao['timestamp']} - {operacao['usuario']}: {operacao['operacao']}")

    def salvar_estado(self):
        """Salva o estado atual do cinema em arquivo"""
        try:
            estado = {
                'estado_cadeiras': self.estado_cadeiras,
                'historico': self.historico
            }

            with open(self.arquivo_estado, 'w') as f:
                json.dump(estado, f)

            print(f"{Fore.GREEN}Estado salvo com sucesso!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Erro ao salvar estado: {e}{Style.RESET_ALL}")

    def recuperar_estado(self):
        """Recupera o estado do cinema de arquivo"""
        try:
            with open(self.arquivo_estado, 'r') as f:
                estado = json.load(f)

            self.estado_cadeiras = estado['estado_cadeiras']
            self.historico = estado['historico']

            print(f"{Fore.GREEN}Estado recuperado com sucesso!{Style.RESET_ALL}")
            return True
        except FileNotFoundError:
            print(f"{Fore.YELLOW}Nenhum estado anterior encontrado.{Style.RESET_ALL}")
            return False
        except Exception as e:
            print(f"{Fore.RED}Erro ao recuperar estado: {e}{Style.RESET_ALL}")
            return False


def menu_principal():
    """Menu principal do sistema de cinema"""
    cinema = Cinema()

    # Tentar recuperar estado anterior
    cinema.recuperar_estado()

    while True:
        print(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'SISTEMA DE GERENCIAMENTO DE CINEMA':^50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

        print("\nOpções disponíveis:")
        print("1 - Ver mapa colorido da sala")
        print("2 - Reservar cadeiras")
        print("3 - Cancelar reservas")
        print("4 - Listar cadeiras disponíveis")
        print("5 - Listar cadeiras indisponíveis")
        print("6 - Mostrar estatísticas")
        print("7 - Ver histórico de operações")
        print("8 - Salvar estado atual")
        print("9 - Sair do sistema")

        try:
            opcao = input(f"\n{Fore.YELLOW}Escolha uma opção (1-9): {Style.RESET_ALL}").strip()

            if opcao == '1':
                cinema.mostrar_mapa_colorido()
            elif opcao == '2':
                usuario = input("Digite seu nome: ").strip()
                cinema.reservar_cadeiras(usuario)
            elif opcao == '3':
                usuario = input("Digite seu nome: ").strip()
                cinema.cancelar_reservas(usuario)
            elif opcao == '4':
                cinema.listar_cadeiras_disponiveis()
            elif opcao == '5':
                cinema.listar_cadeiras_indisponiveis()
            elif opcao == '6':
                cinema.mostrar_estatisticas()
            elif opcao == '7':
                cinema.mostrar_historico()
            elif opcao == '8':
                cinema.salvar_estado()
            elif opcao == '9':
                print(f"{Fore.GREEN}Saindo do sistema...{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Opção inválida! Escolha entre 1 e 9.{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Saindo do sistema...{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}Erro inesperado: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    menu_principal()
