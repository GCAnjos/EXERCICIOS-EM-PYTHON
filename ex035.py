print('-=-'*20)
print('Analisador de segmentos')
print('-=-'*20)
r1 = float(input('Primero segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMA um triangulo!')

