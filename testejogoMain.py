import console
import testejogo

def exibirMenu():
    print("MENU INICIAL DO JOGO")
    print("1 - JOGAR")
    print("2 - CONFIGURACOES")
    print("3 - SAIR")
    print("Escolha uma opcao: ", end='')

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
        testejogo.jogar()
    elif (opcao == 2):
        console.clear()
        testejogo.configurar()
    else:
        print("Bye bye!")
        exit(0)