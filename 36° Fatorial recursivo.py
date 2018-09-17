def fatorialRecursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorialRecursivo(n - 1)


fat = fatorialRecursivo(50)
print(fat)


# Recursividade: A função chama ela mesma

