peso = float(input('Qual e o seu peso? (KG) '))
altura = float(input('Qual e a sua altura? (M) '))
imc = peso / (altura ** 2)
print('O seu IMC e de {:.2f}! Voçê está: '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 18.6 and imc < 25:
    print('COM O PESO IDEAL')
elif imc <= 25.1 and imc < 30:
    print('COM SOBREPESO')
elif imc <= 30.1 and imc < 40:
    print('COM OBESIDADE')
else:
    print('COM OBESIDADE MORBIDA')
