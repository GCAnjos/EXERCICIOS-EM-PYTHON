from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que voçê consegue adibvinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual e o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
