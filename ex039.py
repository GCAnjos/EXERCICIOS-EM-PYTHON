from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Voçê tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Voçe já deveria de se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alisrtamento foi em {}.'.format(ano))

