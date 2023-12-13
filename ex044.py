print('{:=^40}'.format(' LOJAS CARDOSO´S '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {}.'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 200)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS!'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA DE PAGAMENTO! Tente novamente.')
print('Sua compra de {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))

