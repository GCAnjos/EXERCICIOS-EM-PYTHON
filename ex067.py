while True:
    n = int(input('Quer ver a tabua0da de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre!')