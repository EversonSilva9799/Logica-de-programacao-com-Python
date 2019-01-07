import random

matriz =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

linSeg = int(input("Digite a ordem da linha: "))
colSeg = int(input("Digite a ordem da coluna: "))

matriz[0][0] = linSeg
matriz[1][0] = matriz[0][0] + colSeg
matriz[2][0] = matriz[1][0] + colSeg 


for i in range(3):      
    for j in range(3):   
        if matriz[i][j] == 0:
            matriz[i][j] = matriz[i][j-1] + linSeg
               

for i in range(3):
    for j in range(3):
        print("{:2d}" .format(matriz[i][j]), end=" ")
    print("")





