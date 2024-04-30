## Interpreter python3, para executar, use no terminal com python3 ./adivinhacao.py, ou interpretador de costume.

## Jogo da adivinhação de números usando laço FOR
## Uso de funções bultiin e importadas
## Usando o laço for, nos permite colocar uma dinâmica de níveis e pontuação

import random ## Carregando o módulo random para geração de números aleatórios, função importada
import jogos  ## Carregando módulo de menu inicial

def jogar():

    print("*****************************************")
    print("*Bem vindo ao jogo da adivinhação (FOR)!*")
    print("*****************************************")

    usuario = input("Qual seu nome?:")
    numero_secreto = random.randrange(1,51) ## Função para gerar números aleatórios, multiplicado por 100 pois o ramdom gera números reais podendo ser do tipo float, assim pegamos apenas os números antes das casas decimais. A função built-in round() arredonda o valor.
    tentativa = 0 ## Iniciando a contagem das tentativas
    max_tentativa = 0 ## Para o for precisamos gerar um número limitado de tentativas, com o while não é preciso

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

    if(tentativa <= max_tentativa): ## Iniciando o processamento da entrada do usuário
            for tentativa in range(1, max_tentativa +1):
                print(usuario, "esta é a sua {}" .format(tentativa), "º tentativa de {}" .format(max_tentativa)) ## interpolação de string, formata a string para '{}' receber o valor da variável dentro da função format()
                chute = input("Digite um número entre 0 a 50: ") ## Pedindo entrada do usuário
                numero = int(chute) ## convertendo a entrada para um número inteiro para igualdade da função
                acertou = numero == numero_secreto ## Condições de erro / Acerto e informações de proximidade com o número secreto
                errou = numero != numero_secreto
                maior = numero > numero_secreto
                menor = numero < numero_secreto

                if( numero < 1 or numero > 50):
                    print("Você deve digitar um número entre 0 e 50 !")
                    continue ## Control Flow, retorna ao bloco de código anterior

                print("Você digitou", chute) ## Saída para validação do usuário

                if(acertou): ## Função de comparação de igualdade
                        print("***************************")
                        print("**Você acertou", usuario, "!**")
                        print("***************************")
                        print("Você conseguiu usando {}" .format(tentativa),"tentativa(s).") ## Interpolação
                        print("Obrigado por participar, até a próxima !")
                        break ## Parando a execução do laço
                elif(errou):
                    if(maior):
                        print("Você errou", usuario, "seu chute foi maior do que o número secreto")
                        tentativa = tentativa +1
                    elif(menor):
                        print("Você errou", usuario, "seu chute foi menor do que o número secreto")
                        tentativa = tentativa +1
                
                if(tentativa > max_tentativa):
                    print("O número secreto era: ", numero_secreto)
                    print("Acabaram as tentativas, mas você pode iniciar novamente ^^ ")
                    loop = input("Quer tentar novamente? s/n : ") ## Nova entrada do usuario, escolha para seguir no jogo, nessa etapa, o número de tentativas é incrementado em +1
                    if(loop == "s"):
                        jogar()
              
                    else:
                        print("Obrigado por participar", usuario, "até a próxima !")
                        break ## Parando a execução do laço

if(__name__ == "__main__"):
    jogar()