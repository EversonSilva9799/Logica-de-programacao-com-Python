try:
    a = float(input('Digite o numerador: '))  # Este código gera um erro: Divisão por zero não existe
    b = float(input('Digite o denominado: '))
    c = a/b
    print(c)
except ZeroDivisionError: # Caso o erro aconteça será executada essa linha
    print("Não se divide por zero")

