numero = float(input("Digite um número: "))
desconto = float(input(" quer quanto por cento desse número?: "))
num = (desconto/100)*numero
print("O número depois do desconto de {}% é igual a {:.2f}".format(desconto, num))
