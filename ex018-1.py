from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}!'.format(angulo, seno))
coseno = cos(radians(angulo))
print('O angulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
tangente = tan(radians(angulo))
print('O angulo da {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
