cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezesste', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voçê digitou o numero: {cont[num]}')
continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
if continua == 'S':
    num2 = (int(input('Digite um numero entre 0 e 20: ')))
    print(f'Voçê digitou o numero: {cont[num2]}')
else:
    print('Fim.')
