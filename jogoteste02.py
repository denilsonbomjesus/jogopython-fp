from console import *
from time import sleep
from random import randint, randrange 
from jogoConst import *
from jogoMath import solve1, solve2 
import math


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

    birds = [ {"x":0, "y":0, "ativo": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativo": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativo": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativo": False, "traj": {"A":0, "B":0, "C":0}},
              {"x":0, "y":0, "ativo": False, "traj": {"A":0, "B":0, "C":0}}]
    
    pigs = [ { "img":"#", "x":0, "y":0, "ativo": False},
               { "img":"#", "x":0, "y":0, "ativo": False},
               { "img":"#", "x":0, "y":0, "ativo": False}]
    
    pontuacaoJogador = 0.0
    coefAng = 0
    intervalo = 5   # Intervalo de (ciclos de espera para) lançamento de disco
    xcanhao = LIMITE/7
    plataforma = '=' * 3
    ang = -15
    tentativas = 5

    for pig in pigs:  #Desenha os porcos na tela
            pig["ativo"] = True
            pig["x"] = randint(80, 110)
            pig["y"] = randint(20, LIMITE_VERT-5)
            gotoxy(pig["x"], pig["y"])
            print(pig["img"], end='')
            gotoxy(pig["x"] - 1, pig["y"] + 1)
            print(plataforma)
             

    

    a = pig["x"]
    while pig["x"] < (a+10):

            gotoxy(pig["x"], pig["y"])
            print(' ', end='')
            pig["x"]+=1
            gotoxy(pig["x"], pig["y"])
            print('#',end='')
            gotoxy(pig["x"] - 1, pig["y"] + 1)
            print(plataforma)
            gotoxy(pig["x"] - 1, pig["y"] + 1)
            print('   ')

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
                        if not bird["ativo"]:
                            bird["ativo"] = True
                            bird["x"] = xcanhao
                            bird["y"] = LIMITE_VERT-3
                            bird["traj"]["C"] = LIMITE_VERT - 4
                            bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/2 - LIMITE))
                            bird["traj"]["B"] = - bird["traj"]["A"] * (LIMITE - xcanhao)
                            tentativas -= 1
                            break
                elif (ord(c) == ord('a') or ord(c) == ord('A')):
                    ang -= 1
                    bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/4 - LIMITE))
                elif (ord(c) == ord('d') or ord(c) == ord('D')):
                    ang += 1
                    bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/3 - LIMITE))
                elif (ord(c) == ord('z') or ord(c) == ord('Z')):
                    xcanhao -= 1
                elif (ord(c) == ord('c') or ord(c) == ord('C')):
                    xcanhao += 1
                    if xcanhao >= 40:
                        xcanhao -= 1 
            
            for bird in birds: #constrói a trajetória e o movimento do pássaro
                
                if bird["ativo"]:
                    gotoxy(bird["x"], bird["y"])
                    print(' ', end='')

                    bird["x"] += 1
                    bird["x"] = math.floor(bird["x"])
                    bird["y"] = int(solve2(bird["traj"]["A"], bird["traj"]["B"], bird["traj"]["C"], bird["x"]))
                    if (bird["y"] >= LIMITE):
                        bird["ativo"] = False
                    else:
                        gotoxy(bird["x"], bird["y"])
                        print('o',end='')
        
            
            #imprime as tentativas do jogador na tela
            gotoxy((LIMITE / 2) + 8, LIMITE_VERT - 3)
            print(tentativas)

            # Desenha canhão:
            gotoxy(xcanhao, LIMITE_VERT-5)
            print( '\\' if (ang < -15) else ('/' if (ang > -15) else '|'), end='', flush=True)
            
            acertou = False
            for passaro in birds: # vê se o pássaro acertou o alvo
                if passaro["ativo"]:
                    for porco in pigs:
                        if (passaro["x"] == porco["x"] and porco["ativo"]
                            and passaro["y"] == porco["y"]):
                            acertou = True
                            porco["ativo"] = False
                            porco["img"] = ""
                            break

            if acertou:
                pontuacaoJogador += 100
                gotoxy(LIMITE/2 + 3,0)
                print("%0.2f" % pontuacaoJogador, end='')

            fimDoJogo = lambda : pontuacaoJogador == 300
            if (fimDoJogo()):
                clear()
                gotoxy(35, LIMITE_VERT / 2)
                print("VOCÊ GANHOU O JOGO!!!!")
                break
            
            gameOver = lambda : tentativas < 0
            if (gameOver()):
                clear()
                gotoxy(LIMITE/2, LIMITE_VERT / 2)
                print("PERDEU O JOGO, CARA!!!!")
                break
    
            print(end='',flush=True)
            sleep(0.05)
            intervalo -= 1

            if pig["x"] == (a+10):
                while a < pig["x"]:
                    gotoxy(pig["x"], pig["y"])
                    print(' ', end='')
                    pig["x"]-=1
                    gotoxy(pig["x"], pig["y"])
                    print('#',end='')

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
                        if not bird["ativo"]:
                            bird["ativo"] = True
                            bird["x"] = xcanhao
                            bird["y"] = LIMITE_VERT-3
                            bird["traj"]["C"] = LIMITE_VERT - 4
                            bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/2 - LIMITE))
                            bird["traj"]["B"] = - bird["traj"]["A"] * (LIMITE - xcanhao)
                            tentativas -= 1
                            break
                elif (ord(c) == ord('a') or ord(c) == ord('A')):
                    ang -= 1
                    bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/4 - LIMITE))
                elif (ord(c) == ord('d') or ord(c) == ord('D')):
                    ang += 1
                    bird["traj"]["A"] = (max(ang, 4 - bird["traj"]["C"])) / ((LIMITE) * (LIMITE/3 - LIMITE))
                elif (ord(c) == ord('z') or ord(c) == ord('Z')):
                    xcanhao -= 1
                elif (ord(c) == ord('c') or ord(c) == ord('C')):
                    xcanhao += 1
                    if xcanhao >= 40:
                        xcanhao -= 1 
            
            for bird in birds: #constrói a trajetória e o movimento do pássaro
                
                if bird["ativo"]:
                    gotoxy(bird["x"], bird["y"])
                    print(' ', end='')

                    bird["x"] += 1
                    bird["x"] = math.floor(bird["x"])
                    bird["y"] = int(solve2(bird["traj"]["A"], bird["traj"]["B"], bird["traj"]["C"], bird["x"]))
                    if (bird["y"] >= LIMITE):
                        bird["ativo"] = False
                    else:
                        gotoxy(bird["x"], bird["y"])
                        print('o',end='')
        
            
            #imprime as tentativas do jogador na tela
            gotoxy((LIMITE / 2) + 8, LIMITE_VERT - 3)
            print(tentativas)

            # Desenha canhão:
            gotoxy(xcanhao, LIMITE_VERT-5)
            print( '\\' if (ang < -15) else ('/' if (ang > -15) else '|'), end='', flush=True)
            
            acertou = False
            for passaro in birds: # vê se o pássaro acertou o alvo
                if passaro["ativo"]:
                    for porco in pigs:
                        if (passaro["x"] == porco["x"] and porco["ativo"]
                            and passaro["y"] == porco["y"]):
                            acertou = True
                            porco["ativo"] = False
                            porco["img"] = ""
                            break

            if acertou:
                pontuacaoJogador += 100
                gotoxy(LIMITE/2 + 3,0)
                print("%0.2f" % pontuacaoJogador, end='')

            fimDoJogo = lambda : pontuacaoJogador == 300
            if (fimDoJogo()):
                clear()
                gotoxy(35, LIMITE_VERT / 2)
                print("VOCÊ GANHOU O JOGO!!!!")
                break
            
            gameOver = lambda : tentativas < 0
            if (gameOver()):
                clear()
                gotoxy(LIMITE/2, LIMITE_VERT / 2)
                print("PERDEU O JOGO, CARA!!!!")
                break
    
            print(end='',flush=True)
            sleep(0.05)
            intervalo -= 1
    pause()