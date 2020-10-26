

M,N,K = input().split()

M = int(M)
N = int(N)
K = int(K)

sensores = []
raios_seguros = []

for i in range(0,K):
    X,Y,S = input().split()
    X = int(X)
    Y = int(Y)
    S = int(S)
    sensor = [X,Y,S]
    sensores.append(sensor)


print(sensores[1][1])

'''
for j in range(0,K):
     if sensores[k][0] > 5:
         menorraiox = sensor[k][0] - 5
'''
          