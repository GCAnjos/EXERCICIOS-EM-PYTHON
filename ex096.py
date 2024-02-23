def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(l, c)

