import console

def exibirMenu():
    print("MENU INICIAL DO JOGO")
    print("1 - JOGAR")
    print("2 - CONFIGURACOES")
    print("3 - SAIR")
    print("Escolha uma opcao: ", end='')

'''
def jogar():
    print("Jogando...")
    console.pause()
    print("Fim do jogo!")
    console.pause()

def configurar():
    print("Configuracoes do JOGO:")
    print("- Dificuldade:\n  1 - Difícil\n  2 - Médio\n  3 - Fácil")
    console.pause()
    print("Jogo configurado!")
    console.pause()

while True:
    opcao = 0
    while (opcao != 1 and opcao != 2 and opcao != 3):
        console.clear()
        exibirMenu()
        try:
            opcao = int(input())
        except:
            opcao = 0

    if (opcao == 1):
        console.clear()
        jogar()
    elif (opcao == 2):
        console.clear()
        configurar()
    else:
        print("Bye bye!")
        exit(0)
        '''