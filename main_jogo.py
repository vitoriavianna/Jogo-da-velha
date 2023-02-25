import random
joagando = True
num_2 = 1

def main():

    intro = introdução()
    tabuleiro = criar_grade()
    impressão = imprimir(tabuleiro)
    num_1, num_2 = X_ou_O()
    tab_cheio = cheio(tabuleiro, num_1, num_2)






def introdução():
# função que apresenta o jogo, explica as regras e inicia o jogo
    print("Bem vindo ao clássico JOGO DA VELHA \n")
    print("Regras: Player 1 e 2 vão ser representados respesctivamente por X e O revesando turnos \n Marcando espaços vazios em em uma grade 3X3, quem conseguir marcar tres espaços seguidos \n (seja horizontal, vertical ou diagonal), vencerá o jogo!")
    print("BOA SORTE!!!")
    incio = input("você gostaria de jogar: (responda com sim ou nao)")
    if incio == "sim":
        jogando = True
    else :
        jogando = False
    print("aperte enter para continuar \n")





def criar_grade():
# criar uma grade em branco
    print("\n")
    tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return tabuleiro





def X_ou_O():
# Função para decidir quem é X e quem é O
    num_1 = input("Player 1, você será X ou O? ")
    if num_1 == "X":
        num_2 = "O"
        print("Player 2, você é O. ")
    else:
        num_2 = "X"
        print("Player 2, você é X. ")
    input("aperte enter para continuar \n")
    print("\n")
    return num_1 , num_2





def jogo(tabuleiro, num_1, num_2, count):
    if count % 2 == 0:
        player = num_1
    elif count % 2 == 1:
        player = num_2
    print("Player "+ player + ", é sua vez! ")

    linha = int(input("escolha uma linha: \n (linha de cima: 0, linha do meio: 1, linha de baixo: 2):"))
    coluna = int(input("escolha uma coluna: \n (coluna da esquerda: 0, coluna do meio: 1, coluna da direita: 2):"))

    #antes de começarmos a preencher as linhas e colunas da nossa grade de jogo, precisamos verficar duas coisas:
    #se o jogador não escolheu uma coluna inexistente;
    #e se o quadrado que o jogador escolheu ja n esta ocupado

    #verificar se esta dentro da grade:
    while (linha > 2 or linha < 0) or (coluna > 2 or coluna <0):
        fora(linha, coluna)
        linha = int(input("escolha uma linha: \n (linha de cima: 0, linha do meio: 1, linha de baixo: 2):"))
        coluna = int(input("escolha uma coluna: \n (coluna da esquerda: 0, coluna do meio: 1, coluna da direita: 2):"))
    
    #verificar se quadrado ja não está ocupado:
    while (tabuleiro[linha][coluna] == num_1) or (tabuleiro[linha][coluna] == num_2):
        preenchido = proibido(tabuleiro, num_1, num_2, linha, coluna)
        linha = int(input("escolha uma linha: \n (linha de cima: 0, linha do meio: 1, linha de baixo: 2):"))
        coluna = int(input("escolha uma coluna: \n (coluna da esquerda: 0, coluna do meio: 1, coluna da direita: 2):"))

    # agora podemos posicionar na grade
    if player == num_1:
        tabuleiro[linha][coluna] = num_1
            
    else:
        tabuleiro[linha][coluna] = num_2
    
    return (tabuleiro)




def fora(linha, coluna):
    print("você escolheu uma linha ou coluna fora do tabuleiro, escolha outro valor:")




def proibido(tabuleiro, num_1, num_2, linha, coluna):
    print("esse quadrado já está ocupado, tente outro:")



#podemos melhorar nosso jogo imprimindo o tabuleiro de maneira mais bonita :-)
def imprimir(tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro)
    print("---+---+---")
    for k in range(linhas):
        print(tabuleiro[k][0], " |", tabuleiro[k][1], "|", tabuleiro[k][2])
        print("---+---+---")
    return tabuleiro



#nos falta a função q verifica se o tabuleiro está preenchido
def cheio(tabuleiro, num_1, num_2):
    count = 1
    vencedor = True
    while count < 10 and vencedor == True:
        começo = jogo(tabuleiro, num_1, num_2, count)
        impressao = imprimir(tabuleiro)
        
        if count == 9:
            print("Não ha mais espaços vazios \n GAME OVER")
            if vencedor == True:
                print("EMPATE")

        #verificar o vencedor
        vencedor = ver_ganhador(tabuleiro, num_1, num_2, count)
        count += 1
    if vencedor == False:
        print("GAME OVER")
        





#agora vamos criar uma função para verificar quem é o ganhador do nosso jogo, ou se temos um:
def ver_ganhador(tabuleiro, num_1, num_2, count):
    vencedor = True

    #verificar colunas
    for linha in range (0, 3):
        if (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == num_1):
            vencedor = False
            print("Player " + num_1 + ", você venceu campeão!")
   
        elif (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == num_2):
            vencedor = False
            print("Player " + num_2 + ", você venceu campeão!")
    
    #verificar colunas
    for coluna in range (0, 3):
        if (tabuleiro[coluna][0] == tabuleiro[coluna][1] == tabuleiro[coluna][2] == num_1):
            vencedor = False
            print("Player " + num_1 + ", você venceu campeão!")
   
        elif (tabuleiro[coluna][0] == tabuleiro[coluna][1] == tabuleiro[coluna][2] == num_2):
            vencedor = False
            print("Player " + num_2 + ", você venceu campeão!")

    #verificar diagonais
    
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == num_1):
        vencedor = False
        print("Player " + num_1 + ", você venceu campeão!")
   
    elif (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == num_2):
        vencedor = False
        print("Player " + num_2 + ", você venceu campeão!")

    elif (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == num_1):
        vencedor = False
        print("Player " + num_1 + ", você venceu campeão!")
   
    elif (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == num_2):
        vencedor = False
        print("Player " + num_2 + ", você venceu campeão!")

    return vencedor


main()
