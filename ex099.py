from time import sleep


def maior(* num):
    cont = maior = 0
    print('=-=' * 12)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 8, 6, 4, 1)
maior(6, 7, 3)
maior(1, 2)
maior(6)
maior()
