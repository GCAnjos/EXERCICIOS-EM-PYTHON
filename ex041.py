from datetime import date
atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação MIRIM.')
elif idade >= 10 and idade <= 14:
    print('Classificação INFANTIL:')
elif idade >= 15 and idade <= 19:
    print('Classificação JUNIOR.')
elif idade >= 20 and idade <= 25:
    print('Classificação SENIOR.')
else:
    print('Classificação MASTER.')

