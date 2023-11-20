resp = 'S'
media = quant = soma = maior = menor = 0
while resp in 'Ss':
    nun = int(input('Digite um numero: '))
    soma += nun
    quant += 1
    if quant == 1:
        maior = menor = nun
    else:
        if nun > maior:
            maior = nun
        if nun < menor:
            menor = nun
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voçê digitou {} numeros e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
