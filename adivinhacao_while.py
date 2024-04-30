## Interpreter python3, para executar, use no terminal com python3 ./adivinhacao.py, ou interpretador de costume.

## Jogo da adivinhação de números usando laço WHILE
## Uso de funções bultiin e importadas

import random ## Carregando o módulo random para geração de números aleatórios, função importada
import jogos ## Carregando módulo de menu inicial

def jogar():

    print("*******************************************")
    print("*Bem vindo ao jogo da adivinhação (WHILE)!*")
    print("*******************************************")

    usuario = input("Qual seu nome?:")
    numero_secreto = random.randrange(1,51) ## Função para gerar números aleatórios, multiplicado por 100 pois o ramdom gera números reais podendo ser do tipo float, assim pegamos apenas os números antes das casas decimais. A função built-in round() arredonda o valor.
    max_tentativa = 1
    tentativa = 1
    loop = tentativa < max_tentativa

    print("Escolha o nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: ")) ## Necessário transformar a entrada em um número inteiro, pois input só entrende string

    if(nivel == 1):
        max_tentativa = 10 ## Definindo o maximo de tenattivas para o nível
        print("Você tem {}" .format(max_tentativa), "tentativas")
    elif(nivel == 2):
        max_tentativa = 8
        print("Você tem {}" .format(max_tentativa), "tentativas")
    else:
        max_tentativa = 5
        print("Você tem {}" .format(max_tentativa), "tentativas")


    while(tentativa <= max_tentativa):
        print(usuario, "esta é a sua {}" .format(tentativa), "º tentativa") ## interpolação de string, formata a string para '{}' receber o valor da variável dentro da função format()
        chute = input("Digite um número entre 0 e 50: ") ## Pedindo entrada do usuário
        numero = int(chute) ## convertendo a entrada para um número inteiro para igualdade da função
        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if(numero < 0 or numero > 50):
            print("Você deve digitar um número entre 0 e 50 !")
            continue ## Control Flow, retorna ao bloco de código anterior

        print("Você digitou", chute) ## Saída para validação do usuário

        if(acertou): ## Função de comparação de igualdade
                print("***************************")
                print("**Você acertou", usuario, "!**")
                print("***************************")
                print("Você conseguiu com {}" .format(tentativa), "tentativa(s)") ## Interpolação
                print("Obrigado por participar, até a próxima !")
                break
        else:
            if(maior):
                print("Você errou", usuario, "seu chute foi maior do que o número secreto")
            elif(menor):
                print("Você errou", usuario, "seu chute foi menor do que o número secreto")

                if(tentativa < max_tentativa):
                    loop = True ## Nova entrada do usuario, escolha para seguir no jogo, nessa etapa, o número de tentativas é incrementado em +1
                    if(tentativa <= max_tentativa):
                        loop = True
                        tentativa = tentativa +1
                    elif(loop == "n"):
                        tentativa = 50 ## Contradizendo a condição do while para sequencia do jogo
                        print("Obrigado por participar", usuario, "até a próxima !")
                        print("O número secreto era :", numero_secreto)
                        break
                else:
                    print("Acabaram as tentativas, mas você pode iniciar novamente ^^ ")
                    seguir = input("Quer tentar novamente? s/n : ") ## Nova entrada do usuario, escolha para seguir no jogo, nessa etapa, o número de tentativas é incrementado em +1
                    if(seguir == "s"):
                        jogar()
                    else:
                        print("Obrigado por participar", usuario, "até a próxima !")
                        print("O número secreto era :", numero_secreto)
                    break
if(__name__ == "__main__"):
    jogar()