from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota: '))
    nota2 = float(input('Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-=' * 12)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA"}:>8')
print('-' * 36)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 36)
    opc = int(input('Mostra notas de qual  aluno? [COLOCAR O NUMERO DO ALUNO] / (999 INTERROMPE):'))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha [opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')
 
