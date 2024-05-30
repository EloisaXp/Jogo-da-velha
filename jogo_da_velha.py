import random

def mostrar_tabuleiro(matriz):
    for i in range(3):
        print(f" {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ")
        if i <= 1:
             print("---|---|---")

def posicao_coordenadas(posicao):
    coordenadas = []
    if posicao <= 3:
        coordenadas = [0, posicao - 1]
    elif posicao <= 6:
        coordenadas = [1, posicao % 3 - 1]
    else:
        coordenadas = [2, posicao % 3 - 1]
    return coordenadas

def jogada_maquina(matriz):
    posicoes_disponiveis = [(i, j) for i in range(3) for j in range(3) if matriz[i][j] == ' ']
    if posicoes_disponiveis:
        posicao = random.choice(posicoes_disponiveis)
        matriz[posicao[0]][posicao[1]] = 'O'
    return matriz

def verificar_ganhador(matriz):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != " " or matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
            if matriz[i][i] == "X":
                return "jogador"
            else:
                return "máquina"

    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " " or matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        if matriz[1][1] == "X":
            return "jogador"
        else:
            return "máquina"

    if cont == 9:
        return "empate"

def reiniciar_jogo():
    matriz = [[" " for _ in range(3)] for _ in range(3)]
    jogada_maquina(matriz)
    return matriz

def gravar_jogada(arquivo, jogador, posicao):
    arquivo.write(f"{jogador},{posicao[0] + 1},{posicao[1] + 1}\n")

def gravar_resultado(arquivo, resultado):
    arquivo.write(f"Resultado: {resultado}\n\n")

arquivo_jogadas = open("jogadas.txt", "a")

num_partida = 1

while num_partida <= 5:
    matriz = reiniciar_jogo()
    cont = 1
    jogadas = []

    print(f"\nPartida {num_partida}:\n")
    while True:
        if cont % 2 == 1:
            print("Sua vez:")
            mostrar_tabuleiro(matriz)
            x, y = posicao_coordenadas(int(input("Selecione uma das posições (1, 9): ")))
            if matriz[x][y] == " ":
                matriz[x][y] = "X"
                jogadas.append(("jogador", (x, y)))
                cont += 1
            else: 
                print("Posição ocupada. Escolha outra posição: ")
                continue
        else:
            print("Vez da máquina:")
            matriz = jogada_maquina(matriz)
            jogadas.append(("máquina", (x, y)))
            cont += 1

        resultado = verificar_ganhador(matriz)
        if resultado:
            print("Última jogada:")
            mostrar_tabuleiro(matriz)
            if resultado == "jogador":
                print("\n****** Parabéns ******\n     Você ganhou!!\n")
                gravar_resultado(arquivo_jogadas, "Jogador venceu")
            elif resultado == "máquina":
                print("\n***** Máquina ganhou ******\n")
                gravar_resultado(arquivo_jogadas, "Máquina venceu")
            else:
                print("\n****** EMPATE ****** \n")
                gravar_resultado(arquivo_jogadas, "Empate")

            for jogada in jogadas:
                gravar_jogada(arquivo_jogadas, jogada[0], jogada[1])

            opcao = input("Deseja jogar novamente? (s/n): ").lower()
            while opcao not in ['s', 'n']:
                opcao = input("Opção inválida. Deseja jogar novamente? (s/n): ").lower()

            if opcao == 's':
                num_partida += 1
                arquivo_jogadas.write("\n" * 3)  # Separador de partidas
                break
            elif opcao == 'n':
                print("Obrigado por jogar!")
                num_partida = 6
                break

        print()  # Adiciona uma linha em branco entre os tabuleiros

arquivo_jogadas.close()