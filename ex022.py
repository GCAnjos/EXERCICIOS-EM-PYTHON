nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em letra maiuscula é {}!'.format(nome.upper()))
print('Seu nome em letra minuscula é {}!'.format(nome.lower()))
print('Seu nome tem ao todo {} letras!'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras!'.format(nome.find(' ')))

