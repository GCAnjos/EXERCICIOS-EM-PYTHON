from random import randint
computador = randint(0, 5) #Faz o computador "pensar" (no caso sortear um numero)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinha...')
print('-=-'*20)
jogador = int(input('Em que numero pensei? ')) #O jogador tenta adivinha
if jogador == computador:
    print('PARABENS! Voçê consegui me vencer, tambem pensei no {}!'.format(computador)) #Se for o numero correto
else:
    print('GUANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador)) #Se for o numero errado

