lista = []
nomeH = []

lista = input("Quantidade de times e quantidade de alunos?:").split(" ")

times = int((lista[0]))
alunos = int((lista[1]))

print(times)
print(alunos)

x = 0
while x < alunos:
    nometemp = input('Qual o nome do aluno e sua habilidade?: ').split(" ")
    nomeH.append(nometemp)
    x = x+1
print(nomeH)



