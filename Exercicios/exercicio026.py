frase = str(input('Digite uma frase: ')).strip()
print('A letra ¨A¨ aparece {} vezes'.format(frase.upper().count('A')))
print('Aparece a primeira vez na posição {}'.format(frase.upper().find('A')+1))
print('E aparece pela ultima vez na posição {}.'.format(frase.upper().rfind('A')+1))
