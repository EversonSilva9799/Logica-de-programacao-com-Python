#Esta é a primeira forma de fazer
temperaturas_lista = [25,32,21,25,37,35,14,12,3,-5,10]
maior = temperaturas_lista[0]
menor = temperaturas_lista[0]

for temperatura in temperaturas_lista:
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

print(maior)
print(menor)
print('')
#Fim da primeira forma

#Esta é a segunda forma de fazer
max(temperaturas_lista )
min(temperaturas_lista )
print(maior)
print(menor)

    
