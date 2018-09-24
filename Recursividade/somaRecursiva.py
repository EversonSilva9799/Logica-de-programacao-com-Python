def somaRecursiva(n):
    if n == 0:
        return n
    return n + somaRecursiva(n - 1)

print(somaRecursiva(100))
    
