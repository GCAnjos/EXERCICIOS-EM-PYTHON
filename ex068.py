from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voçê jogou {jogador} e o computador {computador}. Total de {total}.', end='')
    print('Deu PAR!' if total % 2 == 0 else 'Deu IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voçê VENCEU!')
            v += 1
        else:
            print('Voçê PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voçê VENCEU!')
            v += 1
        else:
            print('Voçê PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME-OVER! Voçê venceu {v} vezes.')
