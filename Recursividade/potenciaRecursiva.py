def potenciaRecursiva(k, n):
    if n == 0:
        return 1
    return k * potenciaRecursiva(k, n-1)



base = int(input("Base: "))
expoente = int(input("Expoente: "))
print("{}^{} = {}".format(base, expoente, potenciaRecursiva( base, expoente)))


# Explicação

'''

potência de 2 elevado a 3

o primeiro return representa o caso que sabemos, pois
se o expoente for igual a 0 temos: K^0 = 1

Se o n não for zero, segue:

1° n = 3

2 * potenciaRecursiva(2 , 2) | OBS: potenciaRecursiva(2 , 2) = 4
2 * 4 = 8

2° n = 2

2 * potenciaRecursiva(2, 1) | OBS: potenciaRecursiva(2 , 1) = 2
2 * 2 = 4




    
'''
