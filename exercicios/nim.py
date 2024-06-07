def computador_escolhe_jogada(n, m):
    # Computador tenta deixar múltiplo de (m+1) peças para o jogador
    for i in range(1, m+1):
        if (n - i) % (m + 1) == 0:
            return i
    # Se não for possível, tira o máximo possível
    return m if n >= m else n

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada >= 1 and jogada <= m and jogada <= n:
            jogada_valida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador_atual = "usuario"
    else:
        print("Computador começa!")
        jogador_atual = "computador"
    
    while n > 0:
        if jogador_atual == "usuario":
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
            jogador_atual = "computador"
        else:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
            jogador_atual = "usuario"
        
        n -= jogada
        print(f"Agora restam {n} peça(s) no tabuleiro.")
    
    if jogador_atual == "usuario":
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo! Você ganhou!")

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    
    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****")
        partida()
        if input("Digite 'c' se o computador ganhou ou 'u' se você ganhou: ") == 'c':
            placar_computador += 1
        else:
            placar_usuario += 1
    
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input())
    
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
