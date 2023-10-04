largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimesão de {} x {} e sua area e de {}m².'.format(largura, altura, area))
tinta = area / 1.5
print('Para pintar essa parede voçê precisará de {:.2f}L de tinta!'.format(tinta))
