lista = []
lista2 = []

lista = input("cpto da estrada e a dist entre pedágios? Separe-os por espaço!").split(" ")

compri_estr = int((lista[0]))
dis_ped = int((lista[1]))

lista2 = input("Preço por Km e valor por pedágio? Separe-os por espaço!").split(" ")

valorKm = float((lista2[0]))
preco_ped = float((lista2[1]))

pagar_estrada = compri_estr*valorKm
pagar_ped = (compri_estr/dis_ped)*preco_ped

print(pagar_estrada+pagar_ped)
print(lista)
print(lista2)




