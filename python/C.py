N, M, C = input().split()
N = int(N)
M = int(M)
C = int(C) 

linha = []
carros = []
colisoes = []
#quantidade de carros que não sofreram colisões
qtd_carros = C

for i in range(0,C):
    A,B,D = input().split()
    carro = [int(A), int(B), D]
    carros.append(carro)

if M >= N:
    maior_caminho = M
else:
    maior_caminho = N

for i in range(0, maior_caminho):
    #incrmentando posição dos carros
    for j in range(0, C):
        if carros[j][2] == 'N':
            carros[j][1] = carros[j][1] + 1

        elif carros[j][2] == 'S':
            carros[j][1] = carros[j][1] - 1

        elif carros[j][2] == 'L':
            carros[j][0] = carros[j][0] + 1

        elif carros[j][2] == 'O':
            carros[j][0] = carros[j][0] - 1
    
    #avaliando colisões
    for k in range(0, C):
        if k == C-1:
            #avaliando entre carros
            if (carros[k][0] == carros[0][0]) and (carros[k][1] == carros[0][1]):
                colisao = [carros[k][0], carros[k][1]]
                colisoes.append(colisao)
                qtd_carros = qtd_carros - 2
            #avaliando entre carros e colisões já existentes
            else:
                for l in range(0, len(colisoes)):
                    for m in range(0, C):
                        if (carros[m][0] == colisoes[l][0]) and (carros[m][0] == colisoes[l][1]):
                            qtd_carros = qtd_carros - 1
        else:
            #avaliando entre carros
            if (carros[k][0] == carros[k+1][0]) and (carros[k][1] == carros[k+1][1]):
                colisao = [carros[k][0], carros[k][1]]
                colisoes.append(colisao)
                qtd_carros = qtd_carros - 2
            #avaliando entre carros e colisões já existentes
            else:
                for l in range(0, len(colisoes)):
                    for m in range(0, C):
                        if (carros[m][0] == colisoes[l][0]) and (carros[m][0] == colisoes[l][1]):
                            qtd_carros = qtd_carros - 1

print(qtd_carros)
