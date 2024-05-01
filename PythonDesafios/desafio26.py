frase = str(input('Digite uma frase: '))
incidencia = frase.upper().count('A')
primeiroCaso = frase.upper().index('A')
ultimoCaso = frase.upper().rindex('A')
print('A letra a aparece {} vezes nessa frase\n'
      'Aparece a primeira vez no índice {}\n'
      'Aparece a última vez no índice {}'.format(incidencia,primeiroCaso,ultimoCaso))
