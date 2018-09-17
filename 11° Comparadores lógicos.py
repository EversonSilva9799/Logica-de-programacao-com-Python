#Comparadores lógicos

idade = int(input("Qual a sua idade?: "))
if idade >= 18:
    cnh = input("Você tem carteira? (sim ou não): ")
    if cnh.lower() == "sim":
        print("Você pode dirigir!")
    else:
        print('Você não pode dirigir')
else:
    print("Você não pode dirigir!")


