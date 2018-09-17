
A = [[1, 10, 20,6,51],[30, 2, 40,62,5],[50, 60, 3,4,12]]

lin = len(A)
col = len(A[0])


for i in range(lin):
    for j in range(col):
        A[A.index(j)] = str(j)
        print(type(j))

print(type(A[0][2]))


'''
traco = 0
DP = []
baixo_DP = []
produto = 1
for i in range(lin):
    for j in range(col):
        if i == j: #Identifica os elementos da diagonal principal
            DP.append(A[i][j])
            traco += A[i][j] #Soma dos números da diagonal principal
            print(A[i][j])
        if i > j:
            baixo_DP.append(A[i][j])
        if i < j:
            produto = produto*(A[i][j])
print('tr(A) = ',traco)
print('Maior elemento da DP =',max(DP))
print('A soma dos elementos abaixo é',sum(baixo_DP))
print('O produto dos elementos a cima da DP é',produto)
'''

