def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Número inválido')
            

def division_zero(denominador):
    while True:
        try:
            return a / b
        except ZeroDivisionError:
            print('Não é possível dividir por zero')
            b = input_float('Digite o segundo número: ')
            break
            
          
a = input_float('Digite o primeiro número: ')
b = input_float('Digite o segundo número: ')           
division_zero(b)   


print(a / b)

    
