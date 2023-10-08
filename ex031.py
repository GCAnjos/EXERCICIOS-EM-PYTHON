distancia = float(input('Qual e a distancia da sua viagem? '))
print('Voçê esta prestes a começar uma viagem de {} Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será R${:.2f}.'.format(preço))
