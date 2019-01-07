senha = 258642
print('Procurando...')

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for n in range(10):
                    for m in range(10):
                        for u in range(10):
                            for o in range(10):
                                teste = ('{}{}{}{}{}{}{}{}'.format(i, j, k, l, n, m, u, o))
                                if int(teste) == senha:
                                    print('A senha é {}'.format(teste))
                                    break
