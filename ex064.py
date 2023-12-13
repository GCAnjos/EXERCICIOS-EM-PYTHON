nun = cont = soma = 0
nun = int(input('Digite um numero [999 para parar]: '))
while nun != 999:
    soma += nun
    cont += 1
    nun = int(input('Digite um numero [999 para parar]: '))
print('Voçê digitou {} numeros e a soma entre ele e {}.'.format(cont, soma))

