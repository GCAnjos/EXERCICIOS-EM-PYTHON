import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}!'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('O angulo da {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
