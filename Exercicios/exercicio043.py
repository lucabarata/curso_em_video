peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura * altura)
print('Índice de massa corporal: {:.2f}'.format(imc), end=' - ')
if imc < 18.5:
    print('\033[31mABAIXO DO PESO\033[m')
elif imc <= 25:
    print('\033[32mPESO IDEAL\033[m')
elif imc <= 30:
    print('\033[33mSOBREPESO\033[m')
elif imc <= 40:
    print('\033[31mOBESIDADE\033[m')
else:
    print('\033[31mOBESIDADE MORBIDA\033[m')