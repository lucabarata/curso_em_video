from datetime import date
ano = date.today().year
nasci = int(input('Informe seu ano de nascimento, por favor.\nAno: '))
if ano - nasci < 18:
    print('Você deverá se apresentar ao serviço militar em {} anos'.format(18 - (ano - nasci)))
    print('Seu alistamento será no ano de {}.'.format(18 - (ano - nasci) + ano))
elif ano - nasci > 18:
    print('Você deveria ter se apresentado ao serviço militar {} anos atrás.'.format((ano - nasci) - 18))
    print('Seu alistamento foi no ano de {}.'.format((ano - ((ano - nasci) - 18))))
else:
    print('Você deve se apresentar ao serviço militar, pois completou ou completará 18 anos esse ano.')
