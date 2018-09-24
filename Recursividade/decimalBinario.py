def DecimalBinario(n):
    if n <= 1:
        return n
    return  DecimalBinario(int(n/2)) + n % 2
print(DecimalBinario(0))







        
