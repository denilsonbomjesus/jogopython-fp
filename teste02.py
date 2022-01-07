from console import *
from time import sleep
from random import randint, randrange 
from jogoConst import *
from jogoMath import solve1, solve2 


def jogar():

    #Desenha o mapa na tela
    pause()
    init(LIMITE_VERT)
    gotoxy(0, 1)
    print('=' * LIMITE, end='', flush=True)
    reset(0, 1, LIMITE_VERT, LIMITE)
    print('-' * LIMITE, end='', flush=True)
    gotoxy(0, LIMITE_VERT - 4)
    print('=' * LIMITE, end='', flush=True)
    gotoxy((LIMITE / 2) - 5, 0)
    print("Pontos: 0", end='')
    gotoxy((LIMITE / 2) - 5, LIMITE_VERT - 3)
    print("Tentativas:", end='')
    input()

    birds = [ {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativa": False, "traj": {"A":0, "B":0, "C":0}}]
    
    pigs = [ { "img": "Ж", "x":0, "y":0, "ativo": False},
               { "img":"єо̆ҩ", "x":0, "y":0, "ativo": False},
               { "img":"ð", "x":0, "y":0, "ativo": False}]
    
    pontuacaoJogador = 0.0
    coefAng = 0
    intervalo = 5   # Intervalo de (ciclos de espera para) lançamento de disco
    xcanhao = LIMITE/7
    plataforma = '=' * 3
    ang = -15
    tentativas = 5
    porcos = []
    
    for pig in pigs:
            if not pig["ativo"]:
                pig["x"] = randint(80, 120)
                pig["y"] = randint(20, LIMITE_VERT-5) 
                pig["ativo"] = True
                porcos.append(pig)
                gotoxy(pig["x"], pig["y"])
                print(pig["img"], end='')
                gotoxy(pig["x"] - 1, pig["y"] + 1)
                print(plataforma)
    while True:
        #apaga o canhão
        gotoxy(xcanhao, LIMITE_VERT-5)
        print(' ', end='')
        
        #comandos do usuário
        if kbhit():
            c = hitKey()
            gotoxy((xcanhao) - 25, LIMITE_VERT - 3)

            #atirar pássaro
            if ord(c) == ord(' '):
                for bird in birds:
                    if not bird["ativa"]:
                        bird["ativa"] = True
                        bird["x"] = xcanhao
                        bird["y"] = LIMITE_VERT-3
                        bird["traj"]["C"] = bird["y"]
                        bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/2 - LIMITE))
                        bird["traj"]["B"] = - bird["traj"]["A"] * LIMITE
                        tentativas -= 1
                        break
            elif (ord(c) == ord('a') or ord(c) == ord('A')):
                ang -= 1
                bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / (((LIMITE) * (LIMITE - LIMITE))/4)
            elif (ord(c) == ord('d') or ord(c) == ord('D')):
                ang += 1
                bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / (((LIMITE) * (LIMITE - LIMITE))/3)
            elif (ord(c) == ord('z') or ord(c) == ord('Z')):
                xcanhao -= 1
            elif (ord(c) == ord('c') or ord(c) == ord('C')):
                xcanhao += 1
                if xcanhao >= 60:
                    xcanhao -= 1 
            
        
        for bird in birds:
            
            if bird["ativa"]:
                gotoxy(bird["x"], bird["y"])
                print(' ', end='')

                bird["x"] += 2
                bird["y"] = int(solve2(bird["traj"]["A"], bird["traj"]["B"], bird["traj"]["C"], bird["x"]))
                if (bird["y"] >= LIMITE):
                    bird["ativa"] = False
                else:
                    gotoxy(bird["x"], bird["y"])
                    print('o',end='')
        
        #imprime as tentativas do jogador na tela
        gotoxy((LIMITE / 2) + 8, LIMITE_VERT - 3)
        print(tentativas)

         # Desenha canhão:
        gotoxy(xcanhao, LIMITE_VERT-5)
        print( '\\' if (ang < -15) else ('/' if (ang > -15) else '|'), end='', flush=True)

        acertou = 0
        for bird in birds:
            for porco in porcos:
                if (bird["ativa"] and porco["ativo"]
                        and bird["x"] == porco["x"]
                        and bird["y"] == porco["y"]):
                    acertou = True
                    porco["ativo"] = False
                    bird["ativa"] = False
                    break

        if (acertou):
            pontuacaoJogador += 100
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % pontuacaoJogador, end='')

        fimDoJogo = lambda : pontuacaoJogador == 300
        if (fimDoJogo()):
            gotoxy(35, LIMITE_VERT / 2)
            print("YOU WIN!")
            break
        
        gameOver = lambda : tentativas < 0
        if (gameOver()):
            clear()
            gotoxy(LIMITE/2, LIMITE_VERT / 2)
            print("GAME OVER!")
            break
 
        print(end='',flush=True)
        sleep(0.1)
        intervalo -= 1
    
    pause()

jogar()

