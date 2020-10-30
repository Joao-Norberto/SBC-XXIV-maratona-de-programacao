
M,N,C = input().split()
M = int(M)
N = int(N)
C = int(C)
cars = []

for i in range(0,C):
      CarM, CarN, CarC = input().split()
      cars.append([int(CarM), int(CarN), CarC])

print(cars)
