numeros = list()
while True:
    n = int(input(f'Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    r = str(input(f'Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 17)
numeros.sort()
print(f'Voçê digitou os valores {numeros}')
