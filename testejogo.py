from console import *
from time import sleep
from random import randrange
from jogoConst import *
from jogoMath import solve1, solve2

def configurar():
    print("Configuracoes do JOGO:")
    print("- Dificuldade:\n  1 - Difícil\n  2 - Médio\n  3 - Fácil")
    pause()
    print('CONFIGURADO')

def jogar():
    #print("Digite o nome do jogador: ")
    #nomeJogador = str(input())

    pause()
    init(LIMITE_VERT)
    gotoxy(0, 1)
    print('-' * LIMITE, end='', flush=True)
    reset(0, 1, LIMITE_VERT, LIMITE)
    print('*' * LIMITE, end='', flush=True)
    gotoxy(0, LIMITE_VERT - 4)
    print('-' * LIMITE, end='', flush=True)
    gotoxy((LIMITE / 2) - 5, 0)
    print("Pontos: 0", end='')
    gotoxy((LIMITE / 2) - 5, LIMITE_VERT - 3)
    print("Alvos:", end='')
    input()

    balas = [ {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0} },
              {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B": 0} } ]
    #for i in range(0, len(balas)):
    #    balas[i]["ativa"] = False

    discos = [ { "img":"@1", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"@2", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"@3", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} },
               { "img":"@4", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} } ]
    #for j in range(0, len(discos)):
    #    discos[j]["ativo"] = False

    pontuacaoJogador = 0.0
    numeroVidasJogador = 3
    coefAng = 0
    intervalo = 5   # Intervalo de (ciclos de espera para) lançamento de disco

    while True:
        # Lançar disco? Discos são lançados em intervalos.
        if (randrange(15) % len(discos) == 0 and intervalo < 0):
            intervalo = len(discos) + randrange(10)
            j = 0
            for disco in discos:
                if (not disco["ativo"]):
                    disco["ativo"] = True
                    disco["x"] = 0
                    disco["y"] = 8 + randrange(20)
                    disco["traj"]["C"] = disco["y"]
                    disco["traj"]["A"] = (max(-15, 4 - disco["traj"]["C"])) / ((LIMITE/2) * (LIMITE/2 - LIMITE)) # 2 = y min
                    disco["traj"]["B"] = - disco["traj"]["A"] * LIMITE
                    break
                j += 1

        # apaga, move e desenha discos
        j = 0
        for disco in discos:
            # Apaga o disco
            gotoxy(disco["x"], disco["y"])
            print("  ", end='')
            
            # Mostra os discos ativos e suas trajetórias:
            gotoxy((LIMITE / 2) + 3, (LIMITE_VERT - 3) + j)
            if disco["ativo"]:
                # Exibe a trajetória
                print("{0:s} = {1:.2f}x^2 + {2:.2f}x + {3:.2f}".format(
                    disco["img"], disco["traj"]["A"], - disco["traj"]["B"], disco["traj"]["C"]), end='')

                # Muda as posições do disco resolvendo equação da trajetória
                disco["x"] += 2    # Disco se move para direita (aumenta x)
                disco["y"] = int(solve2(disco["traj"]["A"], disco["traj"]["B"], disco["traj"]["C"], disco["x"]))

                if disco["x"] >= LIMITE:
                    disco["ativo"] = False
                else:
                    gotoxy(disco["x"], disco["y"])
                    print(disco["img"], end='') # ou print("@" + chr(ord('1')+j), end='')
            else:
                # Limpa exibição da trajetória
                print(' ' * 30, end='')

            j += 1

        #canhao se fica no canto superior da tela
        xCanhao = LIMITE-118
        yCanhao = LIMITE_VERT/2

        # COMANDOS DO USUÁRIO
        if (kbhit()):
            c = hitKey()
            gotoxy((LIMITE / 2) - 25, LIMITE_VERT - 3)
            print(ord(c), (ord(c) == ord(' ')), end='', flush=True)
            
            # Atirar bala?
            if (ord(c) == ord(' ')): # tecla de espaço em branco usada para disparar
                for bala in balas:
                    if (not bala["ativa"]):
                        bala["ativa"] = True
                        bala["x"] = xCanhao
                        bala["y"] = yCanhao
                        bala["traj"]["A"] = coefAng
                        bala["traj"]["B"] = 2
                        break
            elif (ord(c) == ord('a')) or (ord(c) == ord('A')):
                coefAng = min(coefAng + 1, 3)
            elif (ord(c) == ord('d')) or (ord(c) == ord('D')):
                coefAng = max(-3, coefAng - 1)

            elif (ord(c) == ord('w')) or (ord(c) == ord('W')):
                yCanhao -= 1
            elif (ord(c) == ord('x')) or (ord(c) == ord('X')):
                yCanhao += 1

        # apaga, move e desenha balas
        for bala in balas:
            if (bala["ativa"]):
                gotoxy(bala["x"], bala["y"])
                print(' ', end='')

                #bala["x"] = bala["y"]   # FAZER x da Bala se mover pelo coefAng (bala["traj"]["A"])
                bala["y"] -= bala["traj"]["B"]  # FAZER bala["y"] = solve1(bala["traj"], bala["x"])
                if (bala["y"] <= 3):
                    bala["ativa"] = False
                else:
                    gotoxy(bala["x"], bala["y"])
                    print('o',end='')

        #apagar canhao:
        gotoxy(xCanhao, yCanhao)
        print(' ', end='')

        # Desenha canhão:
        gotoxy(xCanhao, yCanhao)
        print( '/' if (coefAng > 0) else '_', end='', flush=True)

        acertou = 0
        for bala in balas:
            for disco in discos:
                if (bala["ativa"] and disco["ativo"]
                        and bala["x"] == disco["x"]
                        and bala["y"] == disco["y"]):
                    acertou = True
                    disco["ativo"] = False
                    bala["ativa"] = False
                    break

        if (acertou):
            pontuacaoJogador += PONTOS_ACERTO
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % pontuacaoJogador, end='')

        if (pontuacaoJogador < 0):
            numeroVidasJogador -= 1

        fimDoJogo = lambda : pontuacaoJogador >= 1000
        if (fimDoJogo()):
            gotoxy(35, LIMITE_VERT / 2)
            print("YOU WIN!")
            break
        
        gameOver = lambda : numeroVidasJogador == 0
        if (gameOver()):
            gotoxy(35, LIMITE_VERT / 2)
            print("GAME OVER!")
            break

        print(end='',flush=True)
        sleep(0.1)
        intervalo -= 1

    pause()