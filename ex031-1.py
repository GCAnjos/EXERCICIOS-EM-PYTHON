distancia = float(input('Qual e a distancia da sua viagem? '))
print('Voçê esta prestes a começar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será de R${:.2f}.'.format(preço))

