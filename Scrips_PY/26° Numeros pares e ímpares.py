numeros_lista = []
numeros_pares = []
numeros_impares = []

while True:
    numero  = int(input('Digite o número: (0 Para sair)'))
    if numero == 0:
        break
    numeros_lista.append(numero)
for i in numeros_lista:
    if i%2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)
print('Todos os números:',numeros_lista)
print('')
print('Pares:',numeros_pares)
print('')
print('Ímpares:',numeros_impares)
        
