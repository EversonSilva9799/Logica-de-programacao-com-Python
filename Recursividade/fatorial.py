def fatorialRecursivo(n):
    if n == 0:
        return 1
    return n * fatorialRecursivo(n-1)

num = int(input("Fatorial de: "))
print(fatorialRecursivo(num))
