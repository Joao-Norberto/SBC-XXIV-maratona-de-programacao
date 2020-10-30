M, N, K = input().split()
M = int(M)
N = int(N)
K = int(K)

sensores = list()
thief_position = list()

initial_position = [0, 0]
thief_position.append(initial_position)

for i in range(0, K):
    X, Y, S = input().split()
    X = int(X)
    Y = int(Y)
    S = int(S)
    sensor = [X, Y, S]
    sensores.append(sensor)

for i in range(0, K):
    if i == 0:
        distancia_em_cima = sensores[i][0] - sensores[i][2]
        if distancia_em_cima > 0:
            new_position = [0, sensores[i][1]+sensores[i][2]]
            thief_position.append(new_position)
        else:
            distancia_no_lado = sensores[i][1]-sensores[i][2]
            if distancia_no_lado == 0:
                print('N')
                break
            else:
                new_position = [sensores[i][0]+sensores[i][2], 0]
                thief_position.append(new_position)
    elif i == K-1:
        distancia_em_cima = sensores[i][0] - thief_position[i][0]
        distancia_no_lado = sensores[i][1] - sensores[i][2] - thief_position[i][1]
        if distancia_em_cima > 0 or distancia_no_lado > 0:
            print('S')
        else:
            print('N')
    else:
        distancia_em_cima = sensores[i][0] - thief_position[i][0]
        if distancia_em_cima > 0:
            new_position = [thief_position[i][0], sensores[i][1]+sensores[i][2]]
            thief_position.append(new_position)
        else:
            distancia_no_lado = sensores[i][1]-sensores[i][2]-thief_position[i][1]
            if distancia_no_lado == 0:
                print('N')
                break
            else:
                new_position = [sensores[i][0]+sensores[i][2], thief_position[i][1]]
                thief_position.append(new_position)
