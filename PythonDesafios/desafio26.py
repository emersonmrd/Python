frase = str(input('Digite uma frase: ')).strip()
incidencia = frase.upper().count('A')
primeiroCaso = frase.upper().find('A') + 1
ultimoCaso = frase.upper().rindex('A') + 1
print('A letra a aparece {} vezes nessa frase\n'
      'Aparece a primeira vez no índice {}\n'
      'Aparece a última vez no índice {}'.format(incidencia,primeiroCaso,ultimoCaso))
