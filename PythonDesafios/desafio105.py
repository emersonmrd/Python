'''def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    dicionario['total'] = len(n)
    soma = 0
    for i, nota in enumerate(n):
        if i == 0:
            dicionario['maior'] = nota
            dicionario['menor'] = nota
        if nota > dicionario['maior']:
            dicionario['maior'] = nota
        if nota < dicionario['menor']:
            dicionario['menor'] = nota
        soma += nota
    dicionario['media'] = soma / len(n)
    if sit == True:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['media'] >= 6:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario



resp = notas(3.5, 2, 6.5)
print(resp)
help(notas)
'''


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
resp = notas( 5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)