listagem = ('Lápis', 1.86,
            'Borracha', 2.50,
            'Caderno', 17.65,
            'Estojo', 6.70,
            'Transferidor', 8.00,
            'Compasso', 9.90,
            'Mochila', 326.98,
            'Canetas', 25.99,
            'Livro', 35.56)
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 39)

