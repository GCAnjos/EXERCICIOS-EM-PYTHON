def notas(*n, sit=False):
    """
    > Função para analisar notas e situações de varios alunos.
    :param n: Uma ou mais notas dos alunos (aceita varias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RASOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
