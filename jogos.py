import adivinhacao_for
import adivinhacao_while

def escolher_jogo():
    print("*************************")
    print("***Escolha o seu jogo:***")
    print("*************************")

    print("(1) Advinhação usando laço FOR (2) Advinhação usando WHILE")
    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando advinhação usando FOR")
        adivinhacao_for.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação usando WHILE")
        adivinhacao_while.jogar()

if(__name__ == "__main__"):
    escolher_jogo()