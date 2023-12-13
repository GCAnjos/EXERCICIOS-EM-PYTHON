ano = int(input('Que ano voçê quer analisar? '))
if ano % 4 == 0: #O ano que e divisivel por 4 e bissexto
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))

