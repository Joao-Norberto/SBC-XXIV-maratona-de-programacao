
def main():
    N,K = input().split()
    N = int(N)
    K = int(K)
    criminosos = []
    dela = 1
    sup =0
    entradas = input().split()
    for i in entradas:
        criminosos.append((int(i) + 1))
        if criminosos.count(int(i)) == 0:
            criminosos.append(int(i))
    criminosos.sort()
    criminosos.reverse()
    print(criminosos)
    for i in range(0,K):
        sel = criminosos[0]
        sup = sel - 1
        criminosos.pop(criminosos.index(sel))        
        while criminosos.count(sup) > 0 and criminosos[criminosos.index(sup)] != 1:
            criminosos.pop(criminosos.index(sup))
            sup -= 1  
            dela += 1
    print(dela)
main()

        
        

  