telefones = {}
while True:
   nome = input('Digite o nome: ')
   numero = float(input('Digite um número: '))
   telefones[nome] = numero
   sair = input('Deseja Continuar? Sim/Não: ')
   if sair.lower() == 'não':
      break
soma = sum(telefones.values())
nome = max(telefones)
print(nome)
maior = telefones[nome]
print('O maior número é o de {}. O tamanho é {}'.format(nome, maior))

