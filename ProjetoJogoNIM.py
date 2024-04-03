def main():
    
    print("Bem vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))

    if(escolha == 1):
        print("Você escolheu uma partida isolada!")
        print()
        partida()
    elif(escolha ==2):
        print("Você escolheu um campeonato!")
        print()
        campeonato()
    else:
         print("Escolha invalida")




def campeonato():
    contJogador=0
    contComputador=0
    i =1

    while(i<=3):
        print("**** Rodada %d ****" % i)
        if(partida()):
            contComputador+=1
        else:
            contJogador+=1
        i+=1

    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você %d X %d Computador" %(contJogador,contComputador))


def partida():
    
    fimDeJogo = False
    computadorGanhou = False
    jogadorGanhou = False
    verificador = True
    while(verificador):
        n= int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print()
        if(n<m or n<=0 or m<=0):
            print("Por favor, insira numeros válidos!")
        else:
            verificador = False
            
            
    
    if(n % (m+1) ==0):
        print("Você começa!")
        while(n>0):
            n = n - (usuario_escolhe_jogada(n,m))
            if(n!=0):
               print("agora restam %d peças no tabuleiro" %n)
               print()
               n = n-(computador_escolhe_jogada(n,m))
               if(n!=0):
                   print("agora restam %d peças no tabuleiro" %n)
                   print()
               else:
                   fimDeJogo = True
                   computadorGanhou = True
            else:
                fimDeJogo = True
                jogadorGanhou = True
        if(fimDeJogo and computadorGanhou):
            print("Fim do jogo! O computador ganhou!")
            print()
            return True
        elif(fimDeJogo and jogadorGanhou):
            print("Fim do jogo! O jogador ganhou!")
            print()
            return False
    else:
        print("Computador começa!")
        while(n>0):
            n = n - (computador_escolhe_jogada(n,m))
            if(n!=0):
                print("agora restam %d peças no tabuleiro" %n)
                print()
                n = n-(usuario_escolhe_jogada(n,m))
                if(n!=0):
                   print("agora restam %d peças no tabuleiro" %n)
                   print()
                else:
                   fimDeJogo = True
                   jogadorGanhou = True
            else:
                fimDeJogo = True
                computadorGanhou = True
                
        if(fimDeJogo and computadorGanhou):
            print("Fim do jogo! O computador ganhou!")
            print()
            return True
        elif(fimDeJogo and jogadorGanhou):
            print("Fim do jogo! O jogador ganhou!")
            print()
            return False


def computador_escolhe_jogada(n,m):
   
    i=1
    resultado=1
    verificaCondicao = False

    while(i<=m):
        if((n-i)%(m+1) ==0):
            verificaCondicao=True
            resultado = i
        i+=1
        
    if(verificaCondicao):
        print("O computador tirou %d peças" %resultado)
        return resultado
    else:
        print("O computador tirou %d peças" %m)
        return m

    
def usuario_escolhe_jogada(n,m):
    verificador = True

    while(verificador):
        jogada = int(input("Quantas peças você vai tirar? "))
        print()
        if(jogada<=m and jogada>0):
            print("Você tirou %d peças" %jogada)
            verificador = False
        else:
            print("Oops! jogada inválida! Tente de novo.")

    return  jogada

if __name__ == "__main__":
    main()

    
