valor_compra = int(input('Qual o valor da compra: '))
valor_entregue = int(input('Qual o valor entregue: '))

troco = valor_entregue - valor_compra
notas = [100,50,20,10,5,2,1]
cedulas = 0

for i in notas:
    if i <= troco:
        cedulas = cedulas + troco//i
        troco = troco - cedulas*i
        
        print('{} nota(s) de {}'.format(cedulas, i))
        cedulas = 0       
        if troco == 0:
            break
