#include <stdio.h>

int main()
{
    int M = 0, N = 0, K = 0;
    scanf("%d", &M);
    scanf("%d", &N);
    scanf("%d", &K);

    int sensores[K][3];
    int thief_position[K][2];
    int initial_position[2] = {0, 0};

    thief_position[0][0] = initial_position[0];
    thief_position[0][1] = initial_position[1];

    for (int i = 0; i < K; i++)
    {
        int X = 0, Y = 0, S = 0;
        scanf("%d", &X);
        scanf("%d", &Y);
        scanf("%d", &S);

        for (int j = 0; i < 3; i++)
        {
            switch (j)
            {
            case 0:
                sensores[i][j] = X;
                break;
            case 1:
                sensores[i][j] = Y;
                break;
            case 2:
                sensores[i][j] = S;
                break;
            default:
                break;
            }
        }    
    }
    

/*

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

    */

    return 0;
}