
M,N,C = input().split()
N = int(N)
M = int(M)
C = int(C) 
linha = [' ' * M]
mapa = [linha]*N


for i in range(0,C):
    A,B,D = input().split()
    A = int(A) 
    B = int(B)
    aux = mapa[B-1]
    print(aux)
    aux[A-1] = D
    


print(mapa)

           
